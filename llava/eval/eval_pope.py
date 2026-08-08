import os
import json
import argparse


def norm_text(t):
    # question files pad an instruction suffix ("...\nAnswer the question using
    # a single word or phrase."); annotation files don't. Compare on the question only.
    return t.split('\n')[0].strip()


def eval_pope(cur_questions, answers, label_file):
    # Match each answer to its ground-truth label by (image, question) content
    # instead of assuming cur_questions/answers and the label file share line order.
    # Different POPE annotation/question file versions don't always agree on
    # question_id numbering or row order, which silently corrupts a naive zip().
    label_by_key = {}
    for line in open(label_file, 'r'):
        d = json.loads(line)
        label_by_key[(d['image'], norm_text(d['text']))] = d['label']

    pred_list, label_list = [], []
    unmatched = 0
    for question, answer in zip(cur_questions, answers):
        key = (question['image'], norm_text(question['text']))
        if key not in label_by_key:
            unmatched += 1
            continue

        text = answer['text']
        if text.find('.') != -1:
            text = text.split('.')[0]
        text = text.replace(',', '')
        words = text.split(' ')
        pred_list.append(0 if ('No' in words or 'not' in words or 'no' in words) else 1)
        label_list.append(0 if label_by_key[key] == 'no' else 1)

    if unmatched:
        print('Warning: {} / {} answers had no matching ground-truth label and were skipped'.format(
            unmatched, len(cur_questions)))

    pos, neg = 1, 0
    yes_ratio = pred_list.count(1) / len(pred_list)

    TP, TN, FP, FN = 0, 0, 0, 0
    for pred, label in zip(pred_list, label_list):
        if pred == pos and label == pos:
            TP += 1
        elif pred == pos and label == neg:
            FP += 1
        elif pred == neg and label == neg:
            TN += 1
        elif pred == neg and label == pos:
            FN += 1

    print('TP\tFP\tTN\tFN\t')
    print('{}\t{}\t{}\t{}'.format(TP, FP, TN, FN))

    precision = float(TP) / float(TP + FP)
    recall = float(TP) / float(TP + FN)
    f1 = 2*precision*recall / (precision + recall)
    acc = (TP + TN) / (TP + TN + FP + FN)
    print('Accuracy: {}'.format(acc))
    print('Precision: {}'.format(precision))
    print('Recall: {}'.format(recall))
    print('F1 score: {}'.format(f1))
    print('Yes ratio: {}'.format(yes_ratio))
    print('%.3f, %.3f, %.3f, %.3f, %.3f' % (f1, acc, precision, recall, yes_ratio))
    return f1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotation-dir", type=str)
    parser.add_argument("--question-file", type=str)
    parser.add_argument("--result-file", type=str)
    args = parser.parse_args()

    questions = [json.loads(line) for line in open(args.question_file)]
    questions_by_id = {question['question_id']: question for question in questions}
    answers = [json.loads(q) for q in open(args.result_file)]

    f1_scores = []
    for file in sorted(os.listdir(args.annotation_dir)):
        if not (file.startswith('coco_pope_') and file.endswith('.json')):
            continue  # skip stray entries (e.g. an image folder placed here by mistake)
        category = file[10:-5]
        cur_pairs = [(questions_by_id[a['question_id']], a) for a in answers
                     if questions_by_id[a['question_id']]['category'] == category]
        cur_questions = [q for q, _ in cur_pairs]
        cur_answers = [a for _, a in cur_pairs]
        print('Category: {}, # samples: {}'.format(category, len(cur_answers)))
        f1_scores.append(eval_pope(cur_questions, cur_answers, os.path.join(args.annotation_dir, file)))
        print("====================================")
    print('Average F1 score: {}'.format(sum(f1_scores) / len(f1_scores)))

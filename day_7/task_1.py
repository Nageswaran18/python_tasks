import numpy as np
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
import Levenshtein


def calculate_precision(tp,fp):
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)

def calculate_recall(tp,fn):
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)

def calculate_f1_score(precision,recall):
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)

def calculate_cer(gt, pred):
    total_distance = sum(Levenshtein.distance(gt[i], pred[i]) for i in range(len(gt)))
    total_characters = sum(len(gt[i]) for i in range(len(gt)))
    cer = total_distance / total_characters
    return cer

def calculate_wer(gt, pred):
    total_distance = sum(Levenshtein.distance(gt[i].split(), pred[i].split()) for i in range(len(gt)))
    total_words = sum(len(gt[i].split()) for i in range(len(gt)))
    wer = total_distance / total_words
    return wer


def calculate_la(gt, pred):
    correct_lines = sum(1 for i in range(len(gt)) if gt[i] == pred[i])
    la = correct_lines / len(gt)
    return la



def main():
    true_positive=40
    true_nagative=50
    false_positive=10
    false_nagative=8
    
    
    precious = calculate_precision(true_positive,false_positive)
    recall = calculate_recall(true_positive,false_nagative)
    f1_score = calculate_f1_score(precious,recall)
    
    print('precision:', precious)
    print('recall:',recall)
    print('f1_score:',f1_score)
    
    ground_truth_text = ["hello", "world", "python"]
    predicted_text = ["helo", "word", "pytn"]
    
    cer = calculate_cer(ground_truth_text, predicted_text)
    wer = calculate_wer(ground_truth_text, predicted_text)
    
    print("Character Error Rate (CER):", cer)
    print("Word Error Rate (WER):", wer)
    
    la_ground_truth = ["this is line 1", "another line", "last line"]
    la_predicted = ["this is line 1", "other line", "last line"]
    
    la = calculate_la(la_ground_truth, la_predicted)
    print("Line Accuracy (LA):", la)
    

if __name__ == '__main__':
    main()
    
    

# 24accuracy.py by Roger Xu

import math

def ACCURACY(TP, TN, FN, FP):
	accuracy = (TP + TN) / (TP + FN + TN + FP)
	precision = (TP) / (TP + FP)
	recall = (TP) / (TP + FN)
	f1 = (2 * precision * recall) / (precision + recall)

	return accuracy, f1

print(ACCURACY(120, 180, 20, 80))

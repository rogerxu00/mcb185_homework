# 63dust.py by Roger Xu

import sys
import mcb185
import math

def shan_entropy(seq):
	h = 0
	tot_nuc = (A + C + G + T)
	prob_a = A / tot_nuc
	prob_c = C / tot_nuc
	prob_g = G / tot_nuc
	prob_t = T / tot_nuc
	
	if prob_a != 0: h += (prob_a * math.log(prob_a, 2))
	if prob_c != 0: h += (prob_c * math.log(prob_c, 2))
	if prob_g != 0: h += (prob_g * math.log(prob_g, 2))
	if prob_t != 0: h += (prob_t * math.log(prob_t, 2))
	return -h
	
fasta_file = sys.argv[1]
window = int(sys.argv[2])
threshold_entropy = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(fasta_file):
	print(f'>{defline}')
	listseq = list(seq)
	for i in range(len(seq) - window + 1):
		subseq = seq[i:i+window]
		A = subseq.count('A')
		C = subseq.count('C')
		G = subseq.count('G')
		T = subseq.count('T')
		entropy = shan_entropy(subseq)
		if entropy < threshold_entropy:
			for j in range(i, i + window):
				listseq[j] = 'N'
		
		complete_seq = ''.join(listseq)
		print(complete_seq)

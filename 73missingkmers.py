# 73missingkmers.py by Roger Xu and Natalia Martin

import dogma
import itertools
import mcb185
import sys

fasta = sys.argv[1]

for k in range(4, 10):
	kcount = {}
	for defline, seq in mcb185.read_fasta(fasta):
		rev_seq = dogma.revcomp(seq)
		
		for i in range(len(rev_seq) -k +1):
			kmer = rev_seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		
	if len(kcount.keys()) == 4**k: continue
	
	for ktup in itertools.product('ACGT', repeat = k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
	
	sys.exit()

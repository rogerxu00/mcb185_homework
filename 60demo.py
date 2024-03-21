# 60demo.py by Roger Xu

import sys
import mcb185

# Stepping Through FASTA Files
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))
"""
# python3 60demo.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz



# Sequence Composition
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
"""
# python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
# python3 60demo.py ../MCB185/data/C.elegans.fa.gz
# python3 60demo.py ../MCB185/data/D.melanogaster.fa.gz



# if-elif-else Stack
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
"""
# python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
# python3 60demo.py ../MCB185/data/C.elegans.fa.gz
# python3 60demo.py ../MCB185/data/D.melanogaster.fa.gz



# List Variation
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	counts = []
	for i in range(len(nts)): counts.append(0)
	for nt in seq:
		if   nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:           counts[4] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()
"""
# python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
# python3 60demo.py ../MCB185/data/C.elegans.fa.gz
# python3 60demo.py ../MCB185/data/D.melanogaster.fa.gz



# Indexing With str.find()
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN' # should really be defined outside the loop
	counts = [0] * len(nts)
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()
"""
# python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
# python3 60demo.py ../MCB185/data/C.elegans.fa.gz
# python3 60demo.py ../MCB185/data/D.melanogaster.fa.gz



# Counting With str.count()
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN' # should really be defined outside the loop
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print()
"""
# gunzip -c ~/Code/MCB185/data/A.thaliana.fa.gz | grep -v ">" | grep "[^ACGTN]"

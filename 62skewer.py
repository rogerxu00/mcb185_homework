# 62skewer.py by Roger Xu and Yutong Ji

import sys
import mcb185

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[:w].count('G')
	c = seq[:w].count('C')
	comp = (g + c) / w
	if g + c == 0: skew = 0
	else: skew = (g - c) / (g + c)
	print(0, comp, skew)
	for i in range(w, len(seq)):
		if seq[i - w] == 'G': g -= 1
		elif seq[i - w] == 'C': c -= 1
		if seq[i] == 'G': g += 1
		elif seq[i] == 'C': c += 1
		comp = (g + c) / w
		if g + c == 0: skew = 0
		else: skew = (g - c) / (g + c)
		print(i + 1, f'{comp:.3f}, {skew:.3f}')

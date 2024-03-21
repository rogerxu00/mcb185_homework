# 61skewer.py by Roger Xu

import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')

# testing purposes
'print(i, dogma.gc_comp(s), dogma.gc_skew(s))'

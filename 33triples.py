# 33triples.py by Roger Xu

import math

for i in range(1, 100):
	for j in range(i + 1, 100):
		hyp = math.sqrt(i**2 + j**2)
		if hyp % 1 == 0:
			print(i, j, hyp)

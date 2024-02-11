# 43randomdna.py by Roger Xu

import random

nts = 'ACGT'

for i in range(3):
	print(f'>seq-{i+1}', sep='')
	for j in range(random.randint(20, 50)):
		print(random.choice(nts), end='')
	print()
 
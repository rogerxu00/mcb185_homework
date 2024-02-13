# 45dndstats.py by Roger Xu

"""
Theoretical values:
3D6     10.4535
3D6r1   11.9691
3D6x2   13.4517
4D6d1   12.1878
"""

import random

rolls = 1000000

total_3D6 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
	total_3D6 += score
print(total_3D6 / rolls)

total_3D6r1 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1: d = random.randint(1, 6)
		score += d
	total_3D6r1 += score
print(total_3D6r1 / rolls)

total_3D6x2 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: score += d1
		else: score += d2
	total_3D6x2 += score
print(total_3D6x2 / rolls)

total_4D6r1 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)

	if d1 < d2 and d1 < d3 and d1 < d4: score += d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: score += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: score += d1 + d2 + d4
	else: score += d1 + d2 + d3
	total_4D6r1 += score
print(total_4D6r1 / rolls)

# 46savingthrows.py by Roger Xu

"""
Theoretical values:
DC      norm    adv     dis
5       0.795   0.960   0.638
10      0.549   0.799   0.307
15      0.295   0.502   0.084
"""
import random

def roll_normal():
		return random.randint(1, 20)

def roll_advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		return r1
	else:
		return r2

def roll_disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 <= r2:
		return r1
	else:
		return r2

trials = 10000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_normal()
		if rn >= dc:
			success += 1
	print(success / trials)

trials = 10000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_advantage()
		if rn >= dc:
			success += 1
	print(success / trials)

trials = 10000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_disadvantage()
		if rn >= dc:
			success += 1
	print(success / trials)

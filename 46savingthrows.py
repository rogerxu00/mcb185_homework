# 46savingthrows.py by Roger Xu

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

trials = 1000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_normal()
		if rn >= dc:
			success += 1
	print(success / trials)

trials = 1000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_advantage()
		if rn >= dc:
			success += 1
	print(success / trials)

trials = 1000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = roll_disadvantage()
		if rn >= dc:
			success += 1
	print(success / trials)

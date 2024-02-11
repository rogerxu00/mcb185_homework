# 40demo.py by Roger Xu

import random

# prints random number between 0-1
for i in range(5):
	print(random.random())

# prints random sequence of DNA
for i in range(50):
	print(random.choice('ACGT'), end='')
print()

# prints random sequence of DNA without 0.25 odds
for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else: print(random.choice('CG'), end='')
print()

# prints random die roll	
for i in range(3):
	print(random.randint(1, 6))

# prints random Gaussian distribution
for i in range(5):
	print(random.gauss(0.0, 1.0))

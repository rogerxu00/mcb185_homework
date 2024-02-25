# 57birthday.py by Roger Xu, Adele Ferrer, and Natalia Marin

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

duplicates = 0
for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for j in range(people):
		bday = random.randint(1, days - 1)
		calendar[bday] += 1
		if calendar[bday] > 1:
			duplicates += 1
			break

print(duplicates/trials)

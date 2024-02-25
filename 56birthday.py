# 56birthday.py by Roger Xu, Adele Ferrer, and Natalia Marin

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

duplicates = 0
for i in range(trials):
	birthdays = []
	for j in range(people):
		bday = random.randint(1, days)
		if bday in birthdays:
			duplicates += 1
			break
		else:
			birthdays.append(bday)

print(duplicates/trials)

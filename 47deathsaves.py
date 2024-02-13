# 47deathsaves.py by Roger Xu and Khalid

"""
Theoretical values:
die: 0.407
stabilize: 0.406
revive: 0.186
"""

import random

deaths = 0
stabilizations = 0
revives = 0
trials = 10000

for i in range(trials):
	successes = 0
	failures = 0
	while successes < 3 and failures < 3:
		roll = random.randint(1, 20)
		if roll == 1:
			failures += 2
		elif 1 < roll < 10:
			failures += 1
		elif 10 <= roll < 20:
			successes += 1
		elif roll == 20:
			revives += 1
			break
		if failures >= 3:
			deaths += 1
		if successes == 3:
			stabilizations += 1

death_chance = deaths / trials
stabilization_chance = stabilizations / trials
revive_chance = revives / trials

print('die', death_chance)
print('stabilize', stabilization_chance)
print('revive', revive_chance)

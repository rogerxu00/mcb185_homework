# 44randompi.py by Roger Xu and Natalia Martin

import random
import math

def montecarlo_pi():
	incircle = 0
	outcircle = 0
	totalvalues = 0
	
	while True:
		x = random.randint(0, 1)
		y = random.randint(0, 1)
		distance = math.sqrt(x**2 + y**2)
		
		if distance <= 1:
			incircle += 1
		else:
			outcircle += 1
		totalvalues = outcircle + incircle
		pi = incircle / totalvalues
		print(4 * pi)

montecarlo_pi()

# work in progress, need better approximation

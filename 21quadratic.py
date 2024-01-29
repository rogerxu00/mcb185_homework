# 21quadratic.py by Roger Xu

import math

def quadratic(a, b, c):
	x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	return x1, x2
	
print (quadratic(1, -8, 12))
print (quadratic(2, 16, -24))

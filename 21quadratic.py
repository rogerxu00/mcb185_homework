# 21quadratic.py by Roger Xu

import math

def quadratic(a, b, c):
	det = (b**2 - 4 * a * c)

	if det >= 0: return -b + math.sqrt(det) / 2 * a, -b - math.sqrt(det) / 2 * a
	if det < 0: return 'no real root', 'no real root'

print(quadratic(1, -8, 12))
print(quadratic(1, -2, 18))

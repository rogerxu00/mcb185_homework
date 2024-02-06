# 36poisson.py by Roger Xu

import math

def factorial(var):
	if var == 0: return 1
	fac = 1
	for i in range(1, var + 1):
		fac = fac * i
	return fac

def poisson(n, k):
	return ((n ** k) * math.e ** -n / factorial(k))
	
print(poisson(4, 3))
print(poisson(8, 6))
print(poisson(12, 9))

# 35nchoosek.py by Roger Xu

import math

def factorial(var):
	if var == 0: return 1
	fac = 1
	for i in range(1, var + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))
	
print(nchoosek(10, 4))

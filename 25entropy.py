# 25entropy.py by Roger Xu

import math
import sys

def entropy(a, t, c, g):
	if a < 0: sys.exit('error: a cannot be a negative number')
	if t < 0: sys.exit('error: t cannot be a negative number')
	if c < 0: sys.exit('error: c cannot be a negative number')
	if g < 0: sys.exit('error: g cannot be a negative number')

	else:
		A	= a / (a + t + c + g)
		T	= t / (a + t + c + g)
		C	= c / (a + t + c + g)
		G	= g / (a + t + c + g)
	
		if a != 0:
			S =     (A * math.log2(A))
		if t != 0:
			S = S + (T * math.log2(T))
		if c != 0:
			S = S + (C * math.log2(C))
		if g != 0:
			S = S + (G * math.log2(G))
		return abs(S)
		
print(entropy(4, 5, 6, 7))
print(entropy(5, 0, 5, 6))

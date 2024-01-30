# 25entropy.py by Roger Xu

import math

def entropy(a, t, c, g):

	A = a / (a + t + c + g)
	T = t / (a + t + c + g)
	C = c / (a + t + c + g)
	G = g / (a + t + c + g)

	S = 0
	if a != 0: S = S + (A * math.log2(A))
	if t != 0: S = S + (T * math.log2(T))	
	if c != 0: S = S + (C * math.log2(C))
	if g != 0: S = S + (G * math.log2(G))
	return -S
		
print(entropy(4, 5, 6, 7))
print(entropy(0, 5, 6, 7))

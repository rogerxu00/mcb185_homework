# 22oligotemp.py by Roger Xu

import math

def oligotemp(A, C, G, T):
	if(A + T + G + C) <= 13: return((A + T) * 2) + ((G + C) * 4)
	else: return(64.9 + 41 * (G + C - 16.4)) / (A + T + G + C)
	
print(oligotemp(1, 2, 3, 4))
print(oligotemp(2, 3, 4, 5))

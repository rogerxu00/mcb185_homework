# 22oligotemp.py by Roger Xu

import math

def oligotemp(A, C, G, T):
	oligo = ((A + T) * 2) + ((G + C) * 4)
	longeroligo = (64.9 + 41 * (G + C - 16.4)) / (A + T + G + C)
	if(A + T + G + C) <= 13:
		return(oligo)
	else:
		return(longeroligo)
	
print(oligotemp(1, 2, 3, 4))
print(oligotemp(2, 3, 4, 5))

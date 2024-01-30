# 23hydropathy.py by Roger Xu

import math

def hydropathy(AA):
	if AA == 'I': return 4.5
	
	elif AA == 'V': return 4.2
	elif AA == 'L': return 3.8
	elif AA == 'F': return 2.8
	elif AA == 'C': return 2.5
	elif AA == 'M': return 1.9
	elif AA == 'A': return 1.8
	elif AA == 'G': return -0.4
	elif AA == 'T': return -0.7
	elif AA == 'S': return -0.8
	elif AA == 'W': return -0.9
	elif AA == 'Y': return -1.3
	elif AA == 'P': return -1.6
	elif AA == 'H': return -1.6
	elif AA == 'E': return -3.5
	elif AA == 'Q': return -3.5
	elif AA == 'D': return -3.5
	elif AA == 'N': return -3.5
	elif AA == 'K': return -3.9
	elif AA == 'R': return -4.5
	
	else: return 'amino acid not found'

print(hydropathy('I'))
print(hydropathy('B'))

# 55colorname.py by Roger Xu

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

mind = 1000
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		dec = words[2].split(',')
		r = int(dec[0])
		g = int(dec[1])
		b = int(dec[2])
		d = abs(R-r) + abs(G-g) + abs(B-b)
		if d < mind:
			mind = d
			result = color
print(result)

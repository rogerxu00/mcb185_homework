# 53genomestats.py by Roger Xu

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]
vals = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature:
			start = int(words[3])
			end = int(words[4])
			vals.append(end - start + 1)

# Count
for x in vals[1:]:
	vals.sort()
	total = len(vals)
print('count', total)

# Mini/Maxi
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for x in vals:
		if x < mini: mini = x
		if x > maxi: maxi = x
	return mini, maxi
print('minimum, maximum', minmax(vals))

# Mean
def mean(vals):
	total = 0
	for val in vals:
		total += val
	return round(total / len(vals))
print('mean', mean(vals))

# Standard Deviation
def stvd(vals):
	variance = 0
	for val in vals:
		variance += ((val - mean(vals))**2)
	s = math.sqrt(variance/total)
	return round(s)
print('standard deviation', stvd(vals))

# Median
def median(vals):
	if len(vals) % 2 == 0:
		vals.sort()
		m1 = int((len(vals) / 2) - 1)
		m2 = int(m1 + 1)
		med = round((vals[m1] + vals[m2]) / 2)
	else:
		m1 = int(len(vals) // 2)
		med = round(vals[m1])
	return med
print('median', median(vals))

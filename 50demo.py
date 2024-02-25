# 50demo.py by Roger Xu

import math

# Indexes
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])
for nt in seq: print(nt, end='')
print()
for i in range(len(seq)):
	print(i, seq[i])

# Slices
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])
print(s, s[::], s[::1], s[::-1])

# Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])

# Enumerate()
nts = 'ACGT'
for i, nt in enumerate(nts):
	print(i, nt)

# Zip()
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
	print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)
last = nts.pop()
print(last)
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# List()
items = list()
print(items)
items.append('eggs')
print(items)
stuff = []
stuff.append(3)
print(stuff)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# Split()
text = 'good day	to you'
words = text.split()
print(words)
line = '1.41, 2.72, 3.14'
print(line.split(','))

# Join()
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
'if thing in list: idx = list.index(thing)' # only for list or tuple

# Minimum()
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < ini: mini = val
	return mini

# Minmax()
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

# Mean()
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

# Entropy()
def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

# Dkl()
def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(dkl(p1, p2))

# Files
"""
with open(path) as fp:
	for line in fp:
        do_something_with(line)
fp = open(path)
for line in fp:
	do_something_with(line)
fp.close()
"""

# Compressed Files
"""
import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')
"""

# Converting Types
"""
i = int('42')
x = float('0.61803')
"""

# 82transfac.py by Roger Xu

import gzip
import re
import sys
import json

with gzip.open(sys.argv[1], 'rt') as fp:
	transfac = []
	record = {}
	for line in fp:
		line = line.rstrip()
		if line.startswith('ID'):
			record['ID'] = line.split()[1]
		elif line.startswith('PO'):
			record['pwn'] = []
		elif re.search('\d+', line[0]):
			num = line.split()[1:]
			record['pwn'].append({
				'A': num[0],
				'C': num[1],
				'G': num[2],
				'T': num[3]})
		elif line.startswith('//'):
			transfac.append(record)
			record = {}

print(json.dumps(transfac, indent = 4))

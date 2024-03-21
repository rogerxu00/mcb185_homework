# 84splicsites.py by Roger Xu

# NOT COMPLIETED

import gzip
import json
import mcb185
import sys

def print_pwm(pwm):
	print('AC', 'DEMO', f'')
	print('XX')
	print('ID', id)
	print('XX')
	print('DE')		
	print('PO', '       A', '      C', '     G', '      T')	
	for i, n in enumerate(pwm):
		a = n['A']
		c = n['C']
		g = n['G']
		t = n['T']
		print(f'{i+1:<8}{a:<8}{c:<8}{g:<8}{t:<8}')
	print('XX')
	print('//')

introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'intron': continue #shows only intron lines
		chrom = f[0]
		beg = int(f[3])-1
		end = int(f[4])-1
		strand = f[6]
		n = f[5]
		introns.append((chrom, beg, end, strand, n))
print('introns:', len(introns))

dons = []
accs = []
donlen= 6
acclen = 8

for i in range(donlen):
	dons.append({'A':0, 'C':0, 'G':0, 'T': 0})
for i in range(acclen):
	accs.append({'A':0, 'C':0, 'G':0, 'T': 0})
	
for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for c, b, e, s, n in introns:
		if chrom == c: 
			iseq = seq[b:e+1] 
			if len(iseq) < 60: continue
			if s =='-': iseq = mcb185.anti_seq(iseq)
			
			don = iseq[:6]
			for i, nt in enumerate(don):
				dons[i][nt] += 1
			
			acc = iseq[-8:]
			for i, nt in enumerate(acc):
				accs[i][nt] += 1 

print(print_pwm(dons), '')
print(print_pwm(accs), '')

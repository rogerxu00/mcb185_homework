# 83kozak.py by Roger Xu and Kenta Hsu

# ERRORS

import sys
import gzip
import mcb185

path = sys.argv[1]

def store_cds(path):
	cds = []
	with gzip.open(path, 'rt') as file:
		for line in file:
			line = line.rstrip()
			words = line.split()
			
			if words[0] != 'CDS': continue
			if words[1].startswith('j'): continue
			if words[1].startswith('complement(join'): continue
			if words[1].startswith('complement'):
				strand = '-'
				coords = words[1][11:-1]
			else:
				strand = '+'
				coords = words[1]
				
			numbers = coords.split('..')
			start = numbers[0]
			end = numbers[1]
			
			cds.append((start, end, strand))
	return cds
	
cds_list = store_cds(path)

def contig_origin(path):
	with gzip.open(path, 'rt') as file:
		seq_as_list = []
		contig = False
		for line in file:
			words = line.split()
			if words[0] == 'ORIGIN':
				contig = True
				continue
			if contig == True:
				for i, word in enumerate(words):
					if i > 0:
						seq_as_list.append(word)
		seq = ''.join(seq_as_list)
	return seq

def pwm_dict_maker(site_length):
	po = {}
	for i in range(1, site_length+1):
		po[i] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	return po

def kozak_pwm(path):
	cds_list = store_cds(path)
	kozak_pwm = pwm_dict_maker(14)
	seq = contig_origin(path)
	
	for cds in cds_list:
		start = int(cds[0])
		end = int(cds[1])
		if cds[2] == '+':
			kozak = seq[start-9 -1:start+5 -1]

comp_kozak = kozak_pwm(path)

print('AC E.coli')
print('XX')
print('ID E.coli Kozak Consensus')
print('DE')
a = 'A'
c = 'C'
g = 'G'
t = 'T'
po = 'PO'
print(f'{po:<8}{a:<8}{c:<8}{g:<8}{t:<8}')
for position in comp_kozak:
	a = comp_kozak[position]['A']
	c = comp_kozak[position]['C']
	g = comp_kozak[position]['G']
	t = comp_kozak[position]['T']
	print(f'{position:<8}{a:<8}{c:<8}{g:<8}{t:<8}')
print('XX')

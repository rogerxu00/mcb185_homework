# 64profinder.py by Roger Xu

import dogma
import mcb185
import sys

min_length = int(sys.argv[2])

def sixf_trans(seq, min_length):
	translated = []
	for frame in range(3):
		aas = dogma.translate1((seq[frame:])).split('*')
		for aa in aas:
			if 'M' in aa:
				prot = aa[aa.find('M'):]
				if len(prot) >= min_length:
					translated.append(prot)
	return translated

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	oristrand = sixf_trans(seq, min_length)
	revcompstrand = sixf_trans(dogma.revcomp(seq), min_length)
	for prot in revcompstrand:
		oristrand.append(prot)
	for i, prot in enumerate(oristrand):
		print(f'>{defline[:11]}-prot-{i}')
		print(f'{prot}*')

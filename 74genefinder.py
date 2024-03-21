# 74genefinder.py by Roger Xu and Natalia Martin

import mcb185
import sys

fasta = sys.argv[1]
min_len = int(sys.argv[2])

def cds_finder(seq):
	coordinates = {}
	stop_codon = ['TAA', 'TAG', 'TGA']
	start_codon = 'ATG'
	
	for frame in range(3):
		i = frame
		while i < len(seq):
			codon = seq[i:i+3]
			if codon == start_codon:
				start_index = 1
				for j in range(i + 3, len(seq), 3):
					codon = seq[j:j+3]
					if codon in stop_codon:
						stop_index = j
						if stop_index - start_index >= min_len:
							coordinates[start_index] = stop_index + 2
						break
					i = j
	return coordinates

for defline, seq in mcb185.read_fasta(fasta):
	name = defline.split()
	name_sec = defline[0:29]
	rev_seq = mcb185.anti_seq(seq)
	coordin_neg = cds_finder(rev_seq)
	coordin_pos = cds_finder(seq)
	for k, v in coordin_pos.items():
		print(name_sec,'  RefSeq', '  CDS', '  ', k, '  ', v, '  .  ', '+', '  ID=cds')
	for k, v in coordin_neg.items():
		km = len(seq) - k - 1
		vm = len(seq) - v - 1
		print(name_sec,'  RefSeq', '  CDS', '  ', vm, '  ', km, '  .  ', '-', '  ID=cds')

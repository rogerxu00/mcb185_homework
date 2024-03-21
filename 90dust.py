# 90dust.py by Roger Xu

import argparse
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type = int, default = 20,
	help = 'window size [%(default)i]')
parser.add_argument('-e', '--entropy', type = float, default = 1.4,
	help = 'entropy threshold [%(default).3f]')
parser.add.argument('--lower', action = 'store_true', help = 'soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

for defline, seq in mcb185.read_fasta(arg.file):
	print(defline, seq)


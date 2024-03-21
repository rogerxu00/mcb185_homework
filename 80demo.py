# 80demo.py by Roger Xu

# List of Things
print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][3])

d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])



# Arrays and Matrices



# Records
oligo = {
    'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer'
}

catalog = []
catalog.append(oligo)

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)



# Dicts of Lists
kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)



# Complex Data
{
    "locus": "NC_000913",
    "length": 4641652,
    "type": "DNA",
    "definition": "Escherichia coli str. K-12 substr. MG1655, complete...",
    "reference": [
        {
			"authors": "Riley, M., Abe, T., Arnaud, M.B., Berlyn, M.K...",
			"title": "Escherichia coli K-12: a cooperatively...",
			"journal": "Nucleic Acids Res. 34(1), 1-9(2006)",
            "pubmed": 16397293
        },
        {
			"authors": "Hayashi, K., Morooka, N., Yamamoto, Y., Fujita, K...",
            "title": "Highly accurate genome sequences of Escherichia...",
			"journal": "Mol. Syst. Biol. 2, 2006(2006)",
            "pubmed": 16738553
        }
    ]
}



# JSON
truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))

import re
from urllib.request import urlopen  

ids = []
file = open('rosalind_mprt.txt')
for line in file.read().split():
    ids.append(line)
#print(ids)

proteins = {}
for id in ids:                                      
    URL = 'http://www.uniprot.org/uniprot/' + id[0:6] + '.fasta'
    data = urlopen(URL)
    s = str(data.read().decode('utf-8', 'ignore')) 
    #print(s)
    seq = s.split('\n', 1)[1].replace("\n", '')
    #print(seq)
    proteins[id] = seq
#print(proteins)

Nglyco = re.compile(r'(?=(N[^P][ST][^P]))')

for id in proteins:
    positions = []
    for m in re.finditer(Nglyco, str(proteins[id])):
        positions.append(m.start() + 1)
    if len(positions) > 0: 
        print(id)
        print(' '.join(map(str, positions)))
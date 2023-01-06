from Bio import SeqIO
from Bio import Seq

lns = []
for line in SeqIO.parse('rosalind_splc.txt', 'fasta'):
    s = str(line.seq)
    lns.append(s)
#print(lns)

DNA = lns[0]
exons = lns[1:]
#print(DNA)

for ex in exons:
    se = DNA.split(ex)
    DNA =''.join(se)
DNA_str = ''.join(DNA)
#print(DNA_str)

protein = Seq.translate(DNA_str)
print(protein[:-1])
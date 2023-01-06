from Bio import SeqIO
from Bio import Seq
import re
sequence = ''
for line in SeqIO.parse('rosalind_orf.txt', 'fasta'):
    sequence = line.seq
#print(sequence)
rev_sequence = Seq.reverse_complement(sequence)
#print(sequence)
#print(rev_sequence)

orf = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
ORFs = []
for s in re.findall(orf, str(sequence)):
    ORFs.append(s)
for s in re.findall(orf, str(rev_sequence)):
    ORFs.append(s)
o = set(ORFs)

for seq in o:
    protein = Seq.translate(seq)
    print(protein)
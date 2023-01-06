from Bio import SeqIO
from math import factorial

sequence = ''
for line in SeqIO.parse('rosalind_pmch.txt', 'fasta'):
    sequence = line.seq
#print(sequence)

count_AU = 0
count_GC = 0
for nuc in sequence:
    if nuc == 'A':
        count_AU += 1
    if nuc  == 'G':
        count_GC += 1

folds = factorial(count_AU) * factorial(count_GC)
print(folds)
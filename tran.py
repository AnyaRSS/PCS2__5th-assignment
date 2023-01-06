from Bio import SeqIO

sequences = []
for lines in SeqIO.parse('rosalind_tran.txt', 'fasta'):
    seq = str(lines.seq)
    sequences.append(seq)

s = sequences[0]
t = sequences[1]
#print(len(s), len(t))

transitions = 0
transversions = 0
equal = 0
for i in range(len(s)):
    if s[i] == 'A':
        if t[i] == 'A':
            equal += 1
        elif t[i] == 'G':
            transitions += 1
        else:
            transversions += 1
    elif s[i] == 'G':
        if t[i] == 'G':
            equal += 1
        elif t[i] == 'A':
            transitions += 1
        else:
            transversions += 1
    elif s[i] == 'T':
        if t[i] == 'T':
            equal += 1
        elif t[i] == 'C':
            transitions += 1
        else:
            transversions += 1
    else:
        if t[i] == 'C':
            equal += 1
        elif t[i] == 'T':
            transitions += 1
        else:
            transversions += 1

#print(transitions)
#print(transversions)
#print(equal)

print(transitions/transversions)


#  GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT   
#  vs=v=vv====v====s==v=s=sv=s======v======s======vv=s====s===vs=====s=ss=svvssss=v=
#  TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT
from Bio import SeqIO
sequences = []
ids = []
for line in SeqIO.parse('rosalind_grph.txt', 'fasta'):
    seq = str(line.seq)
    sequences.append(seq)
    id = str(line.id)
    ids.append(id)
#print(sequences)
#print(ids)

pref = []
suff = []
for s in sequences:
    p = s[0:3]
    pref.append(p)
    su = s[-3::]
    suff.append(su)
#print(pref)
#print(suff)

adlist = []
'''for i in range(len(ids)):
    print(ids[i])'''
for x in range(len(pref)):
    for y in range(len(suff)):
        if suff[y] == pref[x]:
            adseq = suff[y], pref[x]
            #print(adseq)
            #print(y, x)
            print(ids[y], ids[x])
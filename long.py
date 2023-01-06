from Bio import SeqIO
sequences = []
for line in SeqIO.parse('rosalind_long.txt', 'fasta'):
    s = str(line.seq)
    sequences.append(s)
#print(sequences)

overlaps = []
overlapping = []
for i in range(len(sequences)):
    t = sequences[i]
    for j in range(len(t) // 2, len(t)):
        suff = t[-(j + 1):]
        for k in range(len(sequences)):
            c = sequences[k]
            for l in range(len(c) // 2, len(c)):
                pref = c[:l]
                if suff == pref:
                    overlaps.append(k)
                    overlapping.append([len(suff), i, k])
#print(overlaps)
#print(overlapping)

s = set(overlaps)
#print(s)
first_read = ''
count = len(overlapping)
for m in range(len(overlapping)):
    suf_index = overlapping[m][1]
    if suf_index not in s:
        first_read = suf_index
        new_str = sequences[overlapping[m][1]] + sequences[overlapping[m][2]][overlapping[m][0]:]
        count -= 1
        pref_index = overlapping[m][2]
        while count > 0:
            for n in range(len(overlapping)):  
                if pref_index == overlapping[n][1]:
                    new_str += sequences[overlapping[n][2]][overlapping[n][0]:]
                    pref_index = overlapping[n][2]
                    count -= 1

print(new_str)
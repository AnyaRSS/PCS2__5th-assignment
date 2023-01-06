from Bio import SeqIO
s = []
for line in SeqIO.parse('rosalind_sseq.txt', 'fasta'):
    seq = str(line.seq)
    s.append(seq)
sequence =s[0]
sub = s[1] 
#print(sequence)
#print(sub)

ind = 0                                    
indices = []                             
for i in range(len(sub)):                    
    for j in range(ind, len(sequence)):           
        ind += 1                           
        if len(indices) < len(sub):        
            if sub[i] == sequence[j]:               
                indices.append(ind)      
                break                    
 
res = ''
for i in indices:
    res += str(i) + str(' ')
print(res)
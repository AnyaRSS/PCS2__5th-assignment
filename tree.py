file = open('rosalind_tree.txt')
f = file.readlines()
n = int(f[0])
ad_li = []

for lines in f[1:]:
    l = lines.strip().split(" ")
    ad_li.append(l)
#print(n)
#print(ad_li)
print(n - len(ad_li) - 1)


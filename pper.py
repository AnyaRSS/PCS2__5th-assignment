from math import factorial
file = open('rosalind_pper.txt')
n = ''
k = ''
f = file.read().split()
n = int(f[0])
k = int(f[1])

par_per = factorial(n) / factorial(n-k) 
print(par_per % 10**6)
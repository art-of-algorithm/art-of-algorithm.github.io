 #for more reading and detail https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"
#importing Math function
import math
n=int(raw_input())
a=[True]*n
a[0]=False
a[1]=False
for i in range(2,int(math.sqrt(n))):
    if a[i] is True:
        for j in range(i**2,n,i):
            a[j]=False
for i in range(0,len(a)):
    if a[i]==True:
        print i,

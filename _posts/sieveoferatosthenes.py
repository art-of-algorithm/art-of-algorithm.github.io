impport math
n=int(raw_input())
a=[True]*n
a[0]=False
a[1]=False
for i in range(2,math.sqrt(n)):
    if a[i] is True:
        for j in range(i**2,n,i):
            a[j]=False
for i in range(0,len(a)):
    if a[i]==True:
        print i,

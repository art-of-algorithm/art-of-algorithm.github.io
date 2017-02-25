#another yet most efficient approach uses O(N) complexity
n=int(raw_input())
m=-1
for i in range(1,n+1):
    j=(n*n-2*n*i)/(2*n-2*i)
    k=n-i-j
    if i*i+j*j==k*k and j>0 and k>0:
        m=max(m,i*j*k)
print ok

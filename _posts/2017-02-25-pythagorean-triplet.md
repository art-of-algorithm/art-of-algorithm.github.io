---
layout: post
title:  "Pythagorean Triplet"
categories: implementation
author: "Rahul"
---


```python
#finding pythagorean triplet for a given N O(N^3) Complexity
def pythagorestriplet(num):
    n=num
    m=1
    for x in range(1,n+1):
        y=x+1
        z=y+1
        while z<=n:
            while z*z<x*x+y*y:
                z=z+1
            if z*z==x*x+y*y and z<=n:
                prod=x*y*z
                m=max(prod,m)
            y=y+1
    print max
#main program to check above function O(n^2) Complexity
print pythagorestriplet(n)

for a in range(1,n):
    for b in range(a,n):
        c=n-a-b
        if c>0:
            if c*c ==a*a+b*b:
                print a*b*c
                break



#another yet most efficient approach uses O(N) complexity
n=int(raw_input())
m=-1
for i in range(1,n+1):
    j=(n*n-2*n*i)/(2*n-2*i)
    k=n-i-j
    if i*i+j*j==k*k and j>0 and k>0:
        m=max(m,i*j*k)
print ok
```
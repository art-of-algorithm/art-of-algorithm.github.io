---
layout: post
title:  "Median of two sorted arrays"
categories: implementation mathematics
author: "Rahul"
---

Program for finding median of two sorted arrays

```python
 def median(arr,n):
	if n%2==0:
		return (arr[n/2]+arr[n/2-1])/2
	else:
		return arr[n/2]
def getmedian(arr1,arr2,n):
	if n<=0:
		return "-1"
	if n==1:
		return (arr1[0]+arr2[0])/2
	if n==2:
		return max((arr1[0],arr2[0])+min(arr1[1],arr2[1]))
m1=median(arr1,n)
m2=median(arr2,n)
if m1==m2:
	return m1
if m1<m2:
	if n%2==0:
		return getmedian(arr1+n/2 -1,arr2,n-n/2+1)
	return getmedian(arr1+n/2,arr1,n-n/2)
if m1>m2:
	if n%2==0:
		return getmedian(arr2+n/2-1,arr1,n-n/2)
	return getmedian(arr2+n/2,arr1,n-n/2)
#Driver Program
arr1=[1,2,3,6]
arr2=[4,6,8,10]
n1=len(arr1)
n2=len(arr2)
if (n1==n2):
	getmedian(arr1,arr2,n1)
else:
	print "doesn't work for unequal size arrays"

   
```
    
        
        

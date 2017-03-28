---
layout: post
title:  "Closest Pair(divide and Conquer Aprroach)"
categories: implementation Geometric-Algorithm
author: "Rahul"
---
We are given an array of n points in the plane, and the problem is to find out the closest pair of points in the array. 

```python
from __future__ import generators
def closestpair(l):
	def square(x):
		return x*x
	def sqdist(p,q):
		return square(p[0]-q[0])+square[p[1]-q[1]]
	#We use the pair L[0],L[1] as our initial guess 
	#at a small distance.
	best=[sqdist(L[0],L[1]),(L[0],L[1])]
	def testpair(p,q):
		d=sqdist(p,q)
		if d<best[0]:
			best[0]=d
			best[1]=p,q
	#Merge two sorted lists by y-coordinate
	def merge(A,B):
		i,j=0,0
		while i<len(A) or j<len(B):
			if j>=len(B) or (i<len(A) and A[i][1] <=B[j][1]):
				yield A[i]
				i +=1
			else:
				yield B[j]
				j +=1
	#Find closest pair recursively;
	#returns all points sorted by y coordinate
	def recur(L):
		if len(L)<2:
			return L
		split=len(L)/2
		splitx=L[split][0]
		L=list(merge(recur(L[:split]),recur(L[split:])))
		#Find possible closest pair across split line
		E=[p for p in L if abs(p[0]-splitx)<best[0]]
		for i in range(len(E)):
			for j in range(1,6):
				if i+j<len(E):
					testpair(E[i],E[i+j])
		return L
	L.sort()
	recur(L)
	return best[1]
print closestpair([(0,0),(7,6),(2,20),(12,5),(16,16),(5,8)])
```

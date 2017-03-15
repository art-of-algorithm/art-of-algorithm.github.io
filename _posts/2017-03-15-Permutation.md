---
layout: post
title:  "Permutation"
categories: implementation mathematics
author: "Rahul"
---

Following Program is to generate all permutations of a given list without using inbuilt module in python

```python
def permutations(lis):
	#if list is empty then simply return
	n=len(lis)
	if n==0:
		return 0
	if n==1:
		return [lis]
	#Create an empty list that will store current permutations
	l=[]
	for i in range(n):
		m=lis[i]
		#extract m from the list and
		#create a new remaning list
		remlist=lis[:i]+lis[i+1:]
		for p in permutations(remlist):
			l.append([m]+p)
	return l
#Main Program
data = list('123')
for p in permutations(data):
    print p

```

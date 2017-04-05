---
layout: post
title:  "Search in a Sorted Matrix "
categories: implementation Matrix
author: "Rahul"
---

```python

def search(matrix,n,x):
	i,j=0,n-1
	while(i<n and j>=0):

		if matrix[i][j]==x:
            
			print (i ,j)
            break
		if matrix[i][j]<x:
			i=i+1
		elif matrix[i][j]>x:
			j=j-1
        else:
            print "Element not found"

#Driver Program to test above function
matrix=[[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]
search(matrix,4,33)


```

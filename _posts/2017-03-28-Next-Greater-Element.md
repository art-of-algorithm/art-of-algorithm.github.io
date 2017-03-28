---
layout: post
title:  "Next Greater Element"
categories: implementation stack
author: "Rahul"
---
Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in array. 
Elements for which no greater element exist, consider next greater element as -1.

```python
def NGE(x):
	flag=False
	for i in arr[arr.count(x):]:
		if i>x:
			print i
			flag=True
	if !flag:
		print "-1"

arr=[4,5,2,25]
x=25
NGE(x)

```

---
layout: post
title:  "Euclid(Computing GCD) Algorithm"
categories: implementation mathematics
author: "Rahul"
---
Following is a python program for computing gcd of two numbers using euclid algorithm

```python
#Euclid algorithm for computing gcd of two numbers
def euclid(a,b):
	c=a%b
	if c==0:
		return b
	else:
		return euclid(b,c)
#Main Program
a=int(raw_input())
b=int(raw_input())
print euclid(a,b)

```

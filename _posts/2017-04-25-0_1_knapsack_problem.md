---
layout: post
title:  "0-1 Knapsack"
categories: implementation mathematics
author: "Rahul"
---

Naive approach for implementing 0-1 knapsack problem

```python
def knapsack(W,wt,val,n):
	#Base Case
	if n==0 or W==0:
		return 0
	#If weight of nth item is more than 
	#W(capacity)
	#it can't be included in solution
	if wt[n-1]>W:
		return knapsack(W,wt,val,n-1)
	#Return the maximum of two cases:
	#(1)nth item not included
	#(2)not included
	else:
		return max(knapsack(W-wt[n-1],wt,val,n-1)+val[n-1],knapsack(W,wt,val,n-1))
#main function
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
print knapsack(W,wt,val,n)

```

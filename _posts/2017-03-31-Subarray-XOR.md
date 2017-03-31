---
layout: post
title:  "Xor of all subarrays Xor"
categories: implementation mathematics
author: "Rahul"
---
Given an array of integers, we need to get total XOR of all subarray XORs 
where subarray XOR can be obtained by XORing all elements of it.

```python
#Return XOR of all subarray xors
def totalXorofsubarraysXor(arr,n):
	res=0
	#considering all subarrays
	for i in range(n+1):
		for j in range(i,n+1):
			res=bool(res)^bool(arr[j])
	return res
#Main program
arr=[3,5,2,4,6]
n=len(arr)
print totalXorofsubarraysXor(arr,n)


```

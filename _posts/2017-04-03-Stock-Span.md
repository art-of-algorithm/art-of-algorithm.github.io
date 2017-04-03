---
layout: post
title:  "The Stock span Problem"
categories: implementation stack
author: "Rahul"
---
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock 
and we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

```python
def countspan(arr,n,s):
	#span value of first day is always 1
	s[0]=1
	for i in range(1,n):
		s[i]=1 #Intitalize span value
		j=i-1
		#Traversing to left while the next element on left is
		#smaller than arr[i] 
		while (j>=0 and (arr[i]>arr[j])):
			s[i] +=1
			j=j-1
def print(arr,n):
	for i in xrange(n):
		print arr[i]
#Driver program
arr=[12,34,32,89,16]
n=len(price)
s=[None]*n
# Fill the span values in list S[]
countSpan(arr, n, s)
 
# print the calculated span values
print(s, n)


    
```
    
        
        

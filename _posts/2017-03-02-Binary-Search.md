---
layout: post
title:  "Binary Search"
categories: implementation
author: "Rahul"
---

Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. 
If the value of the search key is less than the item in the middle of the interval, reduce the interval to the lower half. 
Otherwise reduce it to the upper half.
Repeatedly check until the value is found or the interval is empty.
It has a time complexity of O(logn)
```python
#Binary search function for finding an element x
def binarysearch(arr,l,r,x):
    if l<=r:
        mid=l+(r-l)/2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,l,mid-1,x)
        elif arr[mid]<x:
            return binarysearch(arr,mid+1,r,x)
        else:
            return -1
#main program
arr=[4,3,6,8,13]
x=6
res=binarysearch(arr,0,len(arr)-1,x)
if res=-1:
    print "Element not found"
else:
    print "else element present at index %d" %res
    
        
```

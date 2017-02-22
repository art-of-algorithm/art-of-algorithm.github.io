---
layout: post
title:  "Merge Sort"
categories: implementation
author: "Rahul"
---

Function to implement merge sort

```python
def merge(arr,left,mid,right):
    n1=left-mid+1
    n2=right-mid
    #creating two empty array of sizes n1 and n2 
    arr1=[0]*n1
    arr2=[0]*n2
    #copying data of arr in both the arrays
    for i in range(n1):
        arr1[i]=arr[i]
    for i in range(n2):
        arr2[i]=arr[i]
    i=0
    j=0
    k=l
    #while loop for merging two arrays back in a single arrays
    while i<n1 and j<n2:
         if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i=i+1
        if arr2[j]<arr1[i]:
            arr[k]=arr2[j]
            j=j+1
        k=k+1
    #copying remaining elements if any
    while i<n1:
        arr[k]=arr1[i]
        i=i+1
        k=k+1
    while j<n2:
        arr[k]=arr2[j]
        j=j+1
        k=k+1
def mergesort(arr,left,right):
    if left<right:
        mid=(l+r)/2
        #sort for first halves
        mergesort(arr,left,mid)
        #sort for second halves
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)

#main program to test above function
arr=map(int,raw_input().strip().split(' '))
print ("array before sorting is")
for i in range(len(arr)):
    print arr[i],
#calling mergesort function
print ("array after sorting is")
for i in range(len(arr)):
    print arr[i],
    
```
    
        
        

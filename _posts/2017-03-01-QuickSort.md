---
layout: post
title:  "Quick Sort"
categories: implementation sorting
author: "Rahul"
---

Function to implement Quick sort

```python
#partition function of quick sort
def partition(arr,low,high):
    #Taking pivot as last element
    p=arr[high]
    i=-1
    for j in range(1,len(arr)+1):
        if arr[j]<=p:
            i=i+1
            #swapping elements
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
                   

#Quicksort MAin function
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

#main program to test above function
arr=[10,7,8,9,12]
n=len(arr)
quicksort(arr,0,n-1)
for i in range(n):
    print arr[i],
```
 
Alternate implementation of quicksort but uses more memory

```python
def quicksort(arr):
    less=[]
    equal=[]
    greater=[]
    if len(arr) >1:
        pivot=arr[0]
        for i in arr:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                greater.append(i)
        return sort(less)+equal+sort(greater)
    return arr
arr=map(int,raw_input().split(' '))
print quicksort(arr)
```

Simple implementation of quick sort 2 

```python
# Uses python slice notation
def quicksort(arr): 
    if len(arr) <= 1:
            
            return arr
    else:
          return quicksort(
          [x for x in arr[1:] if x<arr[0]]) + [arr[0]] 
          + quicksort([x for x in arr[1:] if x>=arr[0]])
arr=map(int,raw_input().split(' '))
print quicksort(arr)
```     

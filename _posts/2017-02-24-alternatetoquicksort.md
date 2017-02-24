---
layout: post
title:  "Alternate Implementation of Quicksort"
categories: implementation
author: "Rahul"
---

#alternate implementation of quicksort but uses more memory
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



#simple implementation of quick sort 2 
#uses python slice notation
def quicksort(arr): 
    if len(arr) <= 1:
            
            return arr
    else:
          return quicksort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + quicksort([x for x in arr[1:] if x>=arr[0]])
arr=map(int,raw_input().split(' '))
print quicksort(arr)


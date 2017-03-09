---
layout: post
title:  "Insertion Sort"
categories: implementation sorting
author: "Rahul"
---

Function for insertion sort

```python
def insertion(arr):
    #Two loops for comparing elements one by one 
    for i in range(1,len(arr)):
        for j in range(0,i-1):
            if arr[j]>arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp

#size of array to be taken
n = int(raw_input().strip())
#array input of size n
a = map(int, raw_input().strip().split(' '))
#calling insertion sort
insertion(arr)
#printing elements of array after insertion sort
for i in range(0,len(arr)):
    print arr[i],
```
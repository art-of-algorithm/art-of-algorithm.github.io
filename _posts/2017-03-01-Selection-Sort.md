---
layout: post
title:  "Selection Sort"
categories: implementation sorting
author: "Rahul"
---

```python
def selectionsort(arr):
    
    for i in range(len(arr)):
        min_index=0
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_index]=arr[min_index],arr[i]


arr=[6,3,9,1]
selectionsort(arr)
for i in range(len(arr)):
    print arr[i],


#function 2 for Selection Sort
for i in range(len(arr)):
    min_item=min(arr[i:])
    arr[i],arr[arr.index(min_item)]=arr[arr.index(min_item)],arr[i]
    print min_item
```

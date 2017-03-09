---
layout: post
title:  "Binary Search"
categories: implementation searching
author: "Hemang"
---

```python
def binary_search(aList, num):
    """
    Non Recursive
    """
    length = len(aList)
    mid = int((length)/2)
    while (mid>0):
        if num!= aList[mid]:
            if num < aList[mid] :
                aList = aList[:mid]
            else:
                aList = aList[mid:]
            mid = int((len(aList))/2)
        else:
            return True
    return False
aList = [0, 1, 2, 3, 8, 13, 17, 19, 32,  42, 51]
print(binary_search(aList, 3))

def binary_search_recursive(aList, num):
    print(aList)
    print(num)
    mid = int(len(aList)/2)
    print(mid)
    if num == aList[mid]:
        return True
    elif mid < 1 and num!= mid:
        return False
    else:
        if num > aList[mid]:
            return binary_search_recursive(aList[mid:], num)
        else:
            return binary_search_recursive(aList[:mid],num)

aList = [0, 1, 2, 3, 8, 13, 17, 19, 32,  42, 51]
print(binary_search_recursive(aList, 3))
```

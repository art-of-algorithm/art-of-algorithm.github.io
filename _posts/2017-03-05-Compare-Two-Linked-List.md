---
layout: post
title:  "Compare Two Linked List"
categories: implementation linked-lists
author: "Rahul"
---

Compare the data in the nodes of the linked lists to check if they are equal. 
The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. 
Either head pointer given may be null meaning that the corresponding list is empty.

```python
def primefactors(n):
    i=0
    factors=[]
#here primelist is list of all primes of a given no
    p=primelist[i]
    while p<=n:
        if n%p==0:
            factors.append(p)
            n //=p
        else:
            i +=1
            p=primelist[i]
    return factors
```

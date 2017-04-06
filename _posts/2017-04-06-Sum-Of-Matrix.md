---
layout: post
title:  "Sum of matrix"
categories: implementation matrix
author: "Rahul"
---
Consider a N X N matrix where each element is row number divided by column number (integer division), 
i.e. mat[i][j] = floor((i+1)/(j+1)) where 0 <= i < N and 0 <= j < N.
The task is to find the sum of all matrix element.

```python
n=int(raw_input())
matrix=[[[] for i in range(n)] for i in range(n)]
sum=0
for i in range(n):
    for j in range(n):
        matrix[i][j]=floor((i+1)/(j+1))
        sum=sum+matrix[i][j]
print sum

```

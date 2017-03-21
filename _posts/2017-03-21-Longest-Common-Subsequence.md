---
layout: post
title:  "Longest Common Subsequence"
categories: implementation string
author: "Rahul"
---
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous
```python
# A Naive recursive Python implementation of LCS problem
 
def lcs(X, Y, m, n):
 
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
 
 
# Driver program to test the above function
X = raw_input()
Y = raw_input()
print "Length of LCS is ", lcs(X , Y, len(X), len(Y))
```

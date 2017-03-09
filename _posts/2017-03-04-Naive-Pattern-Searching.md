---
layout: post
title:  "Naive Pattern Searching"
categories: implementation string
author: "Rahul"
---
Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
You may assume that n > m.
```python
#Search function fro pattern finding
def search(pattern,string):
    m=len(pattern)
    n=len(string)
    for i in range(n):
        if string[i:i+m]==pattern:
            print i
#main function to implement above function
string = "JJJFHHHDO"
pattern = "JFHH"
search (pattern,string)

```

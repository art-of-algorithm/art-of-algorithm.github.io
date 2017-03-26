---
layout: post
title:  "Longest Balanced Subsequence"
categories: implementation string
author: "Rahul"
---
The following function helps in determining the length of longest balanced subsequence in the string S



```python

def longest(s):
    match = [0] * (len(s) + 1)
    for i in xrange(1, len(s)):
        if s[i] in '({[':
            continue
        open = '({['[')}]'.index(s[i])]
        start = i - 1 - match[i - 1]
        if start < 0: continue
        if s[start] != open: continue
        match[i] = i - start + 1 + match[start - 1]
    best = max(match)
    end = match.index(best)
    return len(s[end + 1 - best:end + 1])
s=raw_input()
print longest(s)
```

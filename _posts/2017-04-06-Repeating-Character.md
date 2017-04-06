---
layout: post
title:  "Maximum Repeating Character"
categories: implementation string
author: "Rahul"
---

Given a string S, find the maximum consecutive repeating character in the string.
```python
from collections import Counter
s=raw_input()
coun=Counter(s)
for letter,count in coun.most_common(1):
    lis= [letter,count]
print lis[0]

```

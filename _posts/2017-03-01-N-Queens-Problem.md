---
layout: post
title:  "N Queen Problem"
categories: implementation mathematics
author: "Rahul"
---
This is a solution of https://www.hackerrank.com/contests/world-codesprint-9/challenges/queens-attack-2
Here is a code in python of above.

```python
import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

s = set()

for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    
    s.add((rObstacle, cObstacle))
#arrays for storing movement of queen (diagonal,up,down,diagonal-left,diagonal-right etc   
mx = [0, 1, 1, 1, 0, -1, -1, -1]
my = [-1, -1, 0, 1, 1, 1, 0, -1]

ans = 0
for i in xrange(8):
    cur_y, cur_x = rQueen, cQueen
    while 0 < cur_y <= n and 0 < cur_x <= n:
        if (cur_y, cur_x) not in s:
            ans += 1
        else:
            break
        cur_y += my[i]
        cur_x += mx[i]
    ans -= 1
print ans

```

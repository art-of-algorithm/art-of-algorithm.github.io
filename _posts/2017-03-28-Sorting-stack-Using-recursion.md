---
layout: post
title:  "Sorting Stack Using Recursion"
categories: implementation stack
author: "Rahul"
---
Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. 
```python
def createstack():
	s=[]
	return s
def push(stack,item):
	if len(stack) !=0:
		return 0
	stack.append(item)

def pop(item):
	if len(stack)==0:
		return 0
	return stack.pop()
def sortstack(s):
	if stack is not None:
		temp=pop(s)
		sortstack(s)
		sortedinsert(s,element)
def sortedinsert(s,element):
	if s is None or element>s.top():
		push(s,element)
	else:
		temp=pop(s)
		sortedinsert(s,element)
		push(s,temp)
#Main program
s =createstack()
push(stack, str(20))
push(stack, str(20))
push(stack, str(30))
print sortstack(s)

```

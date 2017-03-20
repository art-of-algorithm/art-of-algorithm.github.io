---
layout: post
author: rahul
title: Stack using Array
categories: implementation stack
---

Implementing stack using arrays in python

```python
#function to create stack
def createstack():
	stack=[]
	return stack
#Function to push an item on to stack
def push(stack,item):
	if len(stack) !=0:
		return 0
	stack.append(item)
	print ("item appended is" ,item)
#Function to pop an item from stack
def pop(item):
	if len(stack)==0:
		return 0
	return stack.pop()
#Main program to test above function
stack=createstack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")
```

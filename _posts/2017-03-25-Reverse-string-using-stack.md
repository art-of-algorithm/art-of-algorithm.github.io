---
layout: post
title:  "Reverse string using stack "
categories: implementation stack
author: "Rahul"
---

Program in python for reversing a string using stack
```python
#Function for creating stack
def createstack():
	stack=[]
	return stack
#Function for pushing onto stack
def push(stack,item):
	stack.append(item)
#Function for popping an item
def pop(item):
	if len(stack)==0: return 0
	return stack.pop()
#function for reverse string using stack
def reverse(string):
	n=len(string)
	stack=createstack()
	#Push all characters of string on to stack
	for i in range(n):
		push(stack,string[i])
	#Making string empty since all characters are on stack
	string=""
	for i in range(len(stack)):
		string =string+pop(stack)
	return string
#Main program for reversing string 
string="ArtofAlgorithm"
string=reverse(string)
print string

```

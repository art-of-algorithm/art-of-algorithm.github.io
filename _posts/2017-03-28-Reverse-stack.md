---
layout: post
title:  "Reverse Stack Using recursion"
categories: implementation stack
author: "Rahul"
---
Program in Python to reverse stack using recursion

```python
#Recursive function to insert at bottom of the stack
def insertatbottom(stack,item):
	if isempty(stack):
		push(stack,item)
	else:
		temp=pop(stack)
		insertatbottom(stack,item)
		push(stack,temp)
#Recursive function to reverse stack using insertatbottom
def reverse(stack):
	if not isempty(stack):
		temp=pop(stack)
		reverse(stack)
		insertatbottom(stack,temp)
#function to create a stack.It intializes stack size as 0
def createstack():
	stack=[]
	return stack
#Function to check if stack is empty
def isempty(stack):
	return len(stack)==0:
#function to push an element onto the stack
def push(stack,item):
	stack.append(item)
#Function to pop an element from the stack
def pop(stack):
	if isempty(stack):
		return -1
	return stack.pop()

#Function to print the stack
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
 
# Driver program to test above functions
 
stack = createstack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)


    
```
    
        
        

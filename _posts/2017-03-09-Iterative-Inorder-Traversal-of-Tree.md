---
layout: post
title:  "Iterative inorder traversal"
categories: implementation tree
author: "Rahul"
---

Python program for iterative implementation of iterative inorder traversal

```python
class Node:
	def __init__(self,key):
		self.right=None
		self.left=None
		self.data=key
def inorder(root):
	curr=root
	s=[]
	flag=0
	while(flag):
		if curr is not None:
			s.append(curr)
			curr=curr.left
		else:
			if len(s)>0:
				curr=s.pop()
				print curr.data
				curr=curr.right
			else:
				flag=1
#driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inorder(root)

```

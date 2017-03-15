---
layout: post
title:  "nodes at distance k from the root "
categories: implementation tree
author: "Rahul"
---


```python
class Node:
	def __init__(self,key):
		self.data=key
		self.left=None
		self.right=None
#Function to print nodes at distance k from root of the tree
def kdistantnode(root,k):
	if root is None:
		return 0
	if k==0:
		return root.data
	else:
		kdistantnode(root.left,k-1)
		kdistantnode(root.right,k-1)
#Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(8)
 
kdistantnode(root, 2)
```

---
layout: post
title:  "Size of Tree"
categories: implementation tree
author: "Rahul"
---

Python program for determining size of tree.Size of tree is number of elements in a tree.

```python
class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key
def size(node):
	if node is None:
		return 0
	else:
		return (size(node.left)+1+size(node.right))
#driver program to test above function
node=Node(1)
node.left=Node(2)
node.right=Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)


```

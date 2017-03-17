---
layout: post
title:  "Ancestors of a node "
categories: implementation tree
author: "Rahul"
---

```python
class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key
def printancestors(root,target):
	if root is None:
		return False
	if root.data ==target:
		return True
	#if target is present in either left or right subtree
	#then print this node
	if printancestors(root.left,target) or printancestors(root.right,target):
		print root.data
		return True
	else:
		#else return false
		return False
#Driver program to test above function
root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
printancestors(root,7)
#Complexity of above program is O(n) where n is no. of nodes in tree

```

---
layout: post
title:  "Checking Subtree"
categories: implementation tree
author: "Rahul"
---

This program checks whether a binary  tree is a subtree of another tree or not.

```python
class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key
#This function checks if if both given trees are identical or not 
def ifsame(root1,root2):
	#These are base case
	if root1 is None:
		return False
	if root2 is None:
		return False
	return (root1.data==root2.data and ifsame(root1.left,root2.left) and
		ifsame(root1.right,root2.right))
#this function returns true if T1 is parent of T2
def tree(T1,T2):
	if T1 is None:
		return False
	if T2 is None:
		return False
	#check the tree with root as current node
	if ifsame(T1,T2):
		return true
	#if the tree with root as current node doesn't match then
	#try for left and right subtree one by one
	return tree(T1.left,T2) or tree(T1.right,T2)
#Driver program to test above function
#Tree T1
T1 = Node(26)
T1.right = Node(3)
T1.right.right  = Node(3)
T1.left = Node(10)
T1.left.left = Node(4)
T1.left.left.right = Node(30)
T1.left.right = Node(6)
#Tree T2
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if isSubtree(T, S):
    print "Tree 2 is subtree of Tree 1"
else :
    print "Tree 2 is not a subtree of Tree 1"
```

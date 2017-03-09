---
layout: post
title:  "Level Order Traversal"
categories: implementation
author: "Rahul"
---

Function for insertion sort

```python
 #Recursive Python program for level order traversal of Binary Tree
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
#function to print level order traversal of tree
def levelorder(root):
    h=height(root)
    for i in range(1,h+1):
        givenlevel(root,i)
#print nodes of a given level
def givenlevel(root,level):
    if level==0:
        return 0
    elif level==1:
        print root.data
    else:
        givenlevel(root.left,level-1)
        givenlevel(root.right,level-1)
#function to compute height of tree
def height(root):
    if root is None:
        return 0
    else:
        lheight=height(root.left)
        rheight=height(root.right)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
#main program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print "Level order traversal of binary tree is -"
printLevelOrder(root)
```

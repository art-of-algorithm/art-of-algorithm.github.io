---
layout: post
title:  "Tree Traversal"
categories: implementation
author: "Rahul"
---
Trees can be traversed in different ways.
Following are general ways of traversing a tree
1)Depth first traversal
 =>Inorder(left,root,right)
 =>postorder(left,right,root)
 =>preorder(root,left,right)
2)Breadth first traversal
  =>level order traversal
Time complexity : O(n)
sapce complexity:If we don’t consider size of stack for function calls then O(1) otherwise O(n).

```python
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def preorder(root):
    if root:
        #printing value of root node
        print root.data
        #then recur on the left child
        preorder(root.left)
        #then recur on the right child of the tree
        preorder(root.right)
def inorder(root):
    if root:
        #first recur on the left node
        inorder(root.left)
        #printing value of root node
        print root.data
        #then recur on the right child of the tree
        inorder(root.right)
def postorder(root):
    if root:
        #first recur on the left node
        postorder(root.left)
        #then recur on the right node
        postorder(root.right)
        #printing value of root node
        print root.data
#main function to test above code
root=Node(1)
root.left=Node(2)
root.right= Node(3)
root.left.left= Node(4)
root.left.right= Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)
        

```

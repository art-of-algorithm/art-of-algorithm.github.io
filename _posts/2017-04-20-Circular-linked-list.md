---
layout: post
title:  "Circular Linked List"
categories: implementation linked-list
author: "Rahul"
---

Function for implementing Circular linked list

```python
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class CLL:
	def __init__(self):
		self.head=None
	#Function for inserting node at the begining
	def push(self,data):
		ptr1=Node(data)
		temp=self.head
		ptr1.next=self.head
		#if LL is not None 
		#then set the next of last node
		if self.head is not None:

			while(temp.next!=self.head):
				temp=temp.next
			temp.next=ptr1
		else:
			ptr1.next=ptr1 #For first Node
		self.head=ptr1
	#Function to print nodes in a given CLL
	def printCLL(self):
		temp=self.head
		if self.head is not None:
			while(True):
				print temp.data
				temp=temp.next
				if temp==self.head:

					break
#Main program
cll=CLL()
# Created linked list will be 11->2->56->12
cll.push(21)
cll.push(65)
cll.push(20)
cll.push(14)
 
print "Contents of circular Linked List"
cllist.printList()
           

```

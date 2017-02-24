---
layout: post
title:  "Queue Using Two Stacks"
categories: implementation
author: "Hemang"
---

```python
class Node:
    """
    Node of Linked List
    """
    def __init__(self, item=None, link=None):
        self.data = item
        self.next = link


class Stack:
    """
    Stack Implementation using Linked List
    """
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item, self.head)
        self.head = new_node

    def pop(self):
        if not self.isEmpty():
            popped_node = self.head
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return popped_node.data
        else:
            raise IndexError("Trying to remove from empty stack!")

    def isEmpty(self):
        """
        Returns true if stack is empty, otherwise false
        """
        return self.head == None

    def size(self):
        """
        Returns size of stack
        """
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size

    def __str__(self):
        temp = self.head
        res = ''
        while temp:
            res += ' ' + str(temp.data)
            temp = temp.next
        return res


class Queue:
    """
    Queue Implementation using Stack
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())

        self.stack1.push(item)

        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        removed_element = self.stack1.pop()
        return removed_element

    def __str__(self):
        return str(self.stack1)

mstack = Stack()
mstack.push(9)
mstack.push(10)
print(mstack)
mstack.pop()
print(mstack)


mqueue = Queue()
mqueue.enqueue(9)
mqueue.enqueue(10)
print(mqueue)
mqueue.dequeue()
print(mqueue)
```

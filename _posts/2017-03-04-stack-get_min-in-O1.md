---
layout: post
author: Hemang
title: Stack with GetMin() in O(1)
categories: implementation stack
---

Stack in which you can access the minimum element in O(1) time complexity

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


class GetMinStack:
    """
    GetMinStack Implementation using Linked List
    """
    def __init__(self):
        self.stack = Stack()
        self.min = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.min.isEmpty() or self.get_min() >= item:
            self.min.push(item)

    def get_min(self):
        if self.min:
            return self.min.head.data


    def pop(self):
        popped_data = self.stack.pop()
        if not self.min.isEmpty():
            if popped_data == self.get_min():
                self.min.pop()
        return popped_data

    def isEmpty(self):
        """
        Returns true if stack is empty, otherwise false
        """
        return self.stack.isEmpty()

    def size(self):
        """
        Returns size of stack
        """
        return self.stack.size()

    def __str__(self):
        return str(self.stack)

mstack = GetMinStack()
mstack.push(9)
mstack.push(10)
mstack.push(3)
mstack.push(2)
mstack.push(5)
mstack.push(100)
print(mstack)
mstack.pop()
print(mstack)
print(mstack.get_min())
```

---
layout: post
title:  "Stack Using Two Queues"
categories: implementation stack queue
author: "Hemang"
---

```python
class Node:
    def __init__(self, item=None, link=None):
        self.data = item
        self.next = link


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.front == None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.isEmpty():
            removed_element = self.front.data
            if self.front.next:
                self.front = self.front.next
            else:
                self.front = None
                self.rear = None
            return removed_element
        else:
            raise IndexError("Trying to remove from empty queue!")

    def isEmpty(self):
        return self.front == None

    def size(self):
        temp = self.front
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __str__(self):
        temp = self.front
        res = ''
        while temp:
            res += ' ' + str(temp.data)
            temp = temp.next
        return res


class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue1.enqueue(item)

    def pop(self):
        queue_size = self.queue1.size()
        while queue_size != 1 and queue_size > 0:
            self.queue2.enqueue(self.queue1.dequeue())
            queue_size -= 1
        removed_element = self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return removed_element

    def __str__(self):
        return str(self.queue1)

mqueue = Queue()
mqueue.enqueue(10)
mqueue.enqueue(9)
mqueue.enqueue(8)
print(mqueue)
mqueue.dequeue()
print(mqueue)

mstack = Stack()
mstack.push(10)
mstack.push(9)
mstack.push(8)
print(mstack)
mstack.pop()
print(mstack)
```
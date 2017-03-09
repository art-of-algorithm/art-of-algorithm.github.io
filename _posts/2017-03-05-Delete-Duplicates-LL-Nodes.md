---
layout: post
title:  "Delete duplicate-value nodes"
categories: implementation linked-lists
author: "Rahul"
---
Delete duplicate-value nodes from a sorted linked list
Delete as few nodes as possible so that the list does not contain any value more than once. 
The given head pointer may be null indicating that the list is empty
```python
def RemoveDuplicates(head):
    if (head is None):
        return None
    nextitem=head.next
    while(nextitem is not None and head.data == nextitem.data):
        nextitem=nextitem.next
    head.next = RemoveDuplicates(nextitem)
    return head
    
```

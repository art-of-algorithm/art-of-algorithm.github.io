---
layout: post
title:  "Bubble Sort"
categories: implementation
author: "Hemang"
---

General Bubble Sort


```python
def bubble_sort(listOfElements):
    length = len(listOfElements)
    for length in range(len(listOfElements)-1, 0, -1):
        for x in range(length):
            if listOfElements[x] > listOfElements[x+1]:
                listOfElements[x],listOfElements[x+1] = listOfElements[x+1], listOfElements[x]
                print(listOfElements)

bubble_sort([1,2,35,7,2,1,3])
```


Improvement, stops when no exchange takes place.


```python
def improved_bubble_sort(listOfElements):
    length = len(listOfElements) - 1
    exchange = True
    while length > 0 and exchange:
        exchange = False
        for x in range(length):
            if listOfElements[x] > listOfElements[x+1]:
                print("Exchange Happened")
                exchange = True
                listOfElements[x],listOfElements[x+1] = listOfElements[x+1], listOfElements[x]
                print(listOfElements)
        if exchange == False:
            print("No Exchange Happened")
        length -= 1

improved_bubble_sort([1,2,35,7,2,1,3])
```
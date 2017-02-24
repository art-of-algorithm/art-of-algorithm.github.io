def quicksort(arr):
    less=[]
    equal=[]
    greater=[]
    if len(arr) >1:
        pivot=arr[0]
        for i in arr:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                greater.append(i)
        return sort(less)+equal+sort(greater)
    return arr
arr=map(int,raw_input().split(' '))
print quicksort(arr)

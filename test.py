''''
A = [10, 27, 5, 1, 46, 32, 2, 9, 51, 20, 14, 39, 56]

def left(i):
    return (2*i + 1)

def right(i):
    return((2*i) + 2)


def max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l <= (len(A)-1) and A[l] > A[i]:
        largest = l
    else: 
        largest = i
    if r <= (len(A)-1) and A[r] > A[largest]:
        largest = r
    if largest != i:
        largest_temp = A[i]
        A[i] = A[largest]
        A[largest] = largest_temp
        max_heapify(A, largest)

def build_max_heap(A):
    n = len(A)
    for i in range(int(n/2), -1, -1):
        max_heapify(A,i)

print(build_max_heap(A))
print(A)
'''

A = [10, 27, 5, 1, 46, 32, 2, 9, 51, 20, 14, 39, 76, 7, 11, 27]

def parent(i):
    return ((i - 1)/2)

def left(i):
    return (2*i + 1)

def right(i):
    return ((2*i) + 2)


def min_heapify(A,i):
    l = left(i)
    r = right(i)
    if l <= (len(A)-1) and A[l] < A[i]:
        smallest = l
    else: 
        smallest = i
    if r <= (len(A)-1) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        smallest_temp = A[i]
        A[i] = A[smallest]
        A[smallest] = smallest_temp
        min_heapify(A, smallest)

def build_min_heap(A):
    n = len(A)
    for i in range(int(n/2), -1, -1):
        min_heapify(A,i)

print(build_min_heap(A))
print(A)

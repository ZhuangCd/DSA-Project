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

def max_heapify_Nora(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify_Nora(A, largest)


def build_max_heap(A):
    n = len(A)
    for i in range(int(n/2), -1, -1):
        max_heapify(A,i)

print(build_max_heap(A))
print(A)
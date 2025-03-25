# Project Part I – DSK814
# Group members: Egok Shameek, Nóra Balogh

import sys

def createEmptyPQ():
    """Create and return an empty priority queue (min-heap)."""
    return []

def insert(A, e):
    """
    Insert element `e` into the priority queue `A`.
    Maintains the min-heap property by percolating up.
    """
    A.append(e)
    i = len(A) - 1
    while i > 0 and A[parent(i)] > A[i]:
        p = parent(i)
        A[i], A[p] = A[p], A[i]
        i = p

def extractMin(A):
    """
    Remove and return the smallest element from the priority queue `A`.
    Maintains the min-heap property by percolating down.
    """
    if len(A) == 1:
        return A.pop()
    min_elem = A[0]
    A[0] = A.pop()
    min_heapify(A, 0)
    return min_elem

def min_heapify(A, i):
    """
    Ensure the subtree rooted at index `i` maintains the min-heap property.
    This is a recursive downward operation.
    """
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    if right < len(A) and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def parent(i):
    """Return the index of the parent node for node at index `i`."""
    return (i - 1) // 2


if __name__ == "__main__":
    pq = createEmptyPQ()
    
    for line in sys.stdin:
        try:
            insert(pq, int(line.strip()))
        except:
            pass
    
    while pq:
        print(extractMin(pq))

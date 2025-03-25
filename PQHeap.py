# Project Part I – DSK814
# Group members: Egok Shameek, Nóra Balogh

import sys

def createEmptyPQ():
    """Create and return an empty priority queue (min-heap)."""
    return []

def insert(A, e):
    """
    Insert element e into the priority queue A.
    Maintains the min-heap property by percolating up.
    """
    A.append(e)
    i = len(A) - 1 # Index of e
    while i > 0 and A[parent(i)] > A[i]: # While parent is bigger
        p = parent(i)
        A[i], A[p] = A[p], A[i] # Switch parent and child
        i = p # New index of e is i bc it moved up

def extractMin(A):
    """
    Remove and return the smallest element from the priority queue A.
    Maintains the min-heap property by percolating down.
    """
    if len(A) == 1:
        return A.pop()
    min_elem = A[0] # We take out the root as the smallest element
    A[0] = A.pop() # We use the last element to become the root, O(1)
    min_heapify(A, 0) # This takes O(log n)
    return min_elem

def min_heapify(A, i):
    """
    Ensure the subtree rooted at index i maintains the min-heap property.
    This is a recursive downward operation.
    """
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < len(A) and A[left] < A[smallest]: # If left child smaller than parent 
        smallest = left # Assign smallest to the value of a child
    if right < len(A) and A[right] < A[smallest]:
        smallest = right

    if smallest != i: # Here if the smallest have been changed to child's index then:
        A[i], A[smallest] = A[smallest], A[i] # Switch element and child
        min_heapify(A, smallest) # Continue heapify downward

def parent(i):
    """Return the index of the parent node for node at index i."""
    return (i - 1) // 2

# Just to test the code from terminal until we get the PQSort.py file
if __name__ == "__main__":
    pq = createEmptyPQ()
    
    for line in sys.stdin:
        try:
            insert(pq, int(line.strip()))
        except:
            pass
    
    while pq: #while its not empty
        print(extractMin(pq))

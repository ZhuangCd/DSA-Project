import sys


class PriorityQueue:
    """
    A min-heap priority queue implementation using a Python list.
    Supports insert and extractMin operations.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.heap = []  # List Attribute of the object self

    def insert(self, e):
        """
        Insert element e into the priority queue A.
        Maintains the min-heap property by percolating up.
        """
        self.heap.append(e)
        i = len(self.heap) - 1  # Index of e
        while (
            i > 0 and self.heap[self._parent(i)] > self.heap[i]
        ):  # While parent is bigger
            p = self._parent(i)
            self.heap[i], self.heap[p] = (
                self.heap[p],
                self.heap[i],
            )  # Switch parent and child
            i = p  # New index of e is i bc it moved up

    def extractMin(self):
        """
        Remove and return the smallest element from the priority queue A.
        Maintains the min-heap property by percolating down.
        """
        if len(self.heap) == 1:
            return self.heap.pop()
        min_elem = self.heap[0]  # We take out the root as the smallest element
        self.heap[0] = (
            self.heap.pop()
        )  # We use the last element to become the root, O(1)
        self._min_heapify(0)  # This takes O(log n)
        return min_elem

    def _min_heapify(self, i):
        """
        Ensure the subtree rooted at index i maintains the min-heap property.
        This is a recursive downward operation.
        """
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if (
            left < len(self.heap) and self.heap[left] < self.heap[smallest]
        ):  # Check if Index exists and If left child smaller than parent
            smallest = left  # Assign smallest to the value of a child
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if (
            smallest != i
        ):  # Here if the smallest have been changed to child's index then:
            self.heap[i], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[i],
            )  # Switch element and child
            self._min_heapify(smallest)  # Continue heapify downward

    def _parent(self, i):
        """Return the index of the parent node for node at index i."""
        return (i - 1) // 2

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self.heap) == 0


if __name__ == "__main__":
    pq = PriorityQueue()
    for val in [34, 645, 3, -45, 1, 34, 0]:
        pq.insert(val)

    while not pq.is_empty():
        print(pq.extractMin())

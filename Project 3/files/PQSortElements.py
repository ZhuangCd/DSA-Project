import sys
import PQHeap  # This is the group's PQHeap.py from Part I.
from Element import Element

pq = PQHeap.createEmptyPQ()  # Create an empty priority queue.

for line in sys.stdin:
    # A new element is created with the call Element(key, data), which
    # sets values in its key and data fields. This is shown here with an
    # integer as key and an arbitrary string as data. In Part III, data
    # should instead be trees (see the project description for Part III).
    e = Element(int(line), "Some appropriate data")
    # Insert the new Element into the priority queue.
    PQHeap.insert(pq, e)

while len(pq) > 0:
    # Extract the Element from the priority queue with the smallest key.
    e = PQHeap.extractMin(pq)
    # Access and print its fields key and data.
    extractedKey = e.key
    extractedData = e.data
    print(extractedKey)
    print(extractedData)

import sys
import PQHeap

A = [56, 26, 4, 15, 41, 7, 10, 99, 1, 32, 75]
priority_queue = PQHeap.PriorityQueue(A)

pq = PQHeap.PriorityQueue.create_empty_pq(priority_queue)

n = 0
for line in sys.stdin:
    PQHeap.PriorityQueue.insert(pq, int(line))
    n = n + 1

print()
while n > 0:
    print(PQHeap.PriorityQueue.extract_min(pq))
    n = n - 1

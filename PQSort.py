# Reads integers from stdin, sorts them using a min-heap, and prints them

import sys
from PQHeap import createEmptyPQ, insert, extractMin

def main():
    pq = createEmptyPQ()

    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                num = int(line)
                insert(pq, num)
            except ValueError:
                continue 

    while pq:
        print(extractMin(pq))

if __name__ == "__main__":
    main()

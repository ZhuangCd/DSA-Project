import time
import random


def counting_sort_quick(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = []

    for num in arr:
        count[num] += 1

    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

def counting_sort(arr, k):
    n = len(arr)
    output = [0] * n
    count = [0] * (k + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, k + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

unsorted_arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
k = max(unsorted_arr)

# Generate a large input array
unsorted_arr = [random.randint(0, 1000) for _ in range(100000)]
k = max(unsorted_arr)

sorted_arr_quick, time_quick = measure_time(counting_sort_quick, unsorted_arr)
print("Sorted array (quick):", sorted_arr_quick[:10], "...")  # Print only the first 10 elements for brevity
print(f"Execution time (quick): {time_quick:.8f} seconds")

sorted_arr, time_standard = measure_time(counting_sort, unsorted_arr, k)
print("Sorted array (standard):", sorted_arr[:10], "...")  # Print only the first 10 elements for brevity
print(f"Execution time (standard): {time_standard:.8f} seconds")
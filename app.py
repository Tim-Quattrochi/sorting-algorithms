import time

test_arr = [1, 5, 3, 2, 4, 6, 8, 7, 9, 0]


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, comparisons, swaps


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            swaps += 1
    return arr, comparisons, swaps


def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            comparisons += 1
            swaps += 1
        arr[j+1] = key
    return arr, comparisons, swaps


# 1. record current time and store it in a variable. With the time function.
# 2. copy test_arr list to make sure the original list is not mutated.
# 3. call bubble_sort function and store the result in a variable.
# 4. subtract the current time from the time recorded in step 1 to get the time taken to sort the list.
start_time = time.time()
bubble_sort(test_arr.copy())
bubble_sort_time = time.time() - start_time


start_time = time.time()
selection_sort(test_arr.copy())
selection_sort_time = time.time() - start_time


start_time = time.time()
insertion_sort(test_arr.copy())
insertion_sort_time = time.time() - start_time

print(f"[Bubble Sort]: {bubble_sort_time} seconds")
print(f"[Selection Sort]: {selection_sort_time} seconds")
print(f"[Insertion Sort]: {insertion_sort_time} seconds")

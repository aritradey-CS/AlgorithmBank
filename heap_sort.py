def heapify(arr, n, i):
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child of the root exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child of the root exists and is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap the root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the affected sub-tree recursively
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (largest element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


# Example usage
arr = [9, 4, 2, 7, 1, 5, 3, 8, 6]
sorted_arr = heap_sort(arr)

print("Original array:", arr)
print("Sorted array:", sorted_arr)

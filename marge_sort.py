def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1

    return merged


# Example usage
arr = [9, 4, 2, 7, 1, 5, 3, 8, 6]
sorted_arr = merge_sort(arr)

print("Original array:", arr)
print("Sorted array:", sorted_arr)

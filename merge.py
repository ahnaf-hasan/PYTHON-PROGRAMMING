#Let's Start
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Merge the two halves 
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add these
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example 
arr = [100, 90, 70, 60, 40, 30, 50, 10, 20, 80]
sorted_arr = merge_sort(arr)
print(f'Sorted array: {sorted_arr}')

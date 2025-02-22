def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print(f"Sorted array is: {sorted_arr}")

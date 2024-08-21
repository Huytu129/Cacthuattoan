def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Nếu x ở ngay giữa
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    # Nếu không tìm thấy x
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
x = 10

# Chạy binary search
result = binary_search(arr, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

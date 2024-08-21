def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Tìm điểm giữa của mảng
        L = arr[:mid]  # Chia mảng làm đôi
        R = arr[mid:]

        merge_sort(L)  # Sắp xếp nửa đầu
        merge_sort(R)  # Sắp xếp nửa sau

        i = j = k = 0

        # Hợp nhất hai mảng đã sắp xếp
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Kiểm tra nếu còn phần tử nào
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(f"Sorted array is: {arr}")

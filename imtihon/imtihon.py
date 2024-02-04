def buble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list= [15, 3, 8, 12, 5, 1, 18, 7, 10, 0, 6, 17, 14, 4, 19, 2, 11, 13, 16,20]


def binary_search(arr, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return binary_search(arr, mid + 1, high)
        else:
            return binary_search(arr, low, mid - 1)
    else:
        return low


missing_number = binary_search(my_list, 0, len(my_list) - 1)

print("Yo'qligi:", missing_number)


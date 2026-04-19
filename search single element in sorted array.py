# Find single element in sorted array

arr = [1, 1, 2, 3, 3, 4, 4]

low = 0
high = len(arr) - 1

while low < high:
    mid = (low + high) // 2

    # Make mid even
    if mid % 2 == 1:
        mid -= 1

    if arr[mid] == arr[mid + 1]:
        low = mid + 2
    else:
        high = mid

print("Single element:", arr[low])
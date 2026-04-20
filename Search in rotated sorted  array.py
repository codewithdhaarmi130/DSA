# Search in rotated sorted array

arr = [4, 5, 6, 7, 0, 1, 2]
target = int(input("Enter target: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break

    # Left half is sorted
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # Right half is sorted
    else:
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
else:
    print("Element not found")
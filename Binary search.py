# Binary Search

arr = [1, 3, 5, 7, 9]
key = int(input("Enter number to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index:", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
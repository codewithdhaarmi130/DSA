# Lower Bound using Binary Search

arr = [1, 2, 4, 4, 5]
target = int(input("Enter target: "))

low = 0
high = len(arr) - 1
ans = len(arr)

while low <= high:
    mid = (low + high) // 2

    if arr[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Lower bound index:", ans)
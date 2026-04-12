# Next Permutation

arr = [1, 2, 3]

n = len(arr)

# Step 1: Find breakpoint
i = n - 2
while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1

# Step 2: If breakpoint exists, swap
if i >= 0:
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]

# Step 3: Reverse the remaining part
arr[i + 1:] = reversed(arr[i + 1:])

print("Next permutation:", arr)
# Rotate array to the right by k steps

arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n  # handle large k

# Step 1: Reverse whole array
arr.reverse()

# Step 2: Reverse first k elements
arr[:k] = reversed(arr[:k])

# Step 3: Reverse remaining elements
arr[k:] = reversed(arr[k:])

print("Rotated array:", arr)
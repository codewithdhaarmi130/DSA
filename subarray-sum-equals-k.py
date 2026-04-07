# Subarray sum equals k

arr = [1, 2, 3]
k = 3

count = 0

for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        
        if total == k:
            count += 1

print("Total subarrays:", count)
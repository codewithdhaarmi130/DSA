# Find majority element

arr = [2, 2, 1, 2, 3]

count = 0
candidate = None

# Step 1: Find candidate
for num in arr:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

# Step 2: Verify candidate
count = 0
for num in arr:
    if num == candidate:
        count += 1

if count > len(arr) // 2:
    print("Majority element:", candidate)
else:
    print("No majority element")
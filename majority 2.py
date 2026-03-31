# Find elements appearing more than n/3 times

arr = [1, 2, 3, 1, 2, 1, 2]

count1 = 0
count2 = 0
candidate1 = None
candidate2 = None

# Step 1: Find candidates
for num in arr:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1

# Step 2: Verify candidates
count1 = count2 = 0

for num in arr:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1

result = []
if count1 > len(arr) // 3:
    result.append(candidate1)
if count2 > len(arr) // 3:
    result.append(candidate2)

print("Majority elements:", result)
# Rearrange array by sign

arr = [3, -2, 5, -1, -7, 2]

pos = []
neg = []

# Separate positives and negatives
for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

# Merge alternately
result = []
i = 0

while i < len(pos) and i < len(neg):
    result.append(pos[i])
    result.append(neg[i])
    i += 1

# Add remaining elements
while i < len(pos):
    result.append(pos[i])
    i += 1

while i < len(neg):
    result.append(neg[i])
    i += 1

print("Rearranged array:", result)
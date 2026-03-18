arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

# Count frequency
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Find max frequency
max_freq = 0
max_num = None

for key in freq:
    if freq[key] > max_freq:
        max_freq = freq[key]
        max_num = key

print("Number with highest frequency:", max_num)
print("Frequency:", max_freq)
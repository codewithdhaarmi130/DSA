# Count frequency of elements

arr = [1, 2, 2, 3, 1, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequencies:")
for key in freq:
    print(key, "->", freq[key])
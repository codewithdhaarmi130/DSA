# Find single number using XOR

arr = [2, 3, 5, 3, 2]

result = 0

for num in arr:
    result ^= num   # XOR operation

print("Single number is:", result)
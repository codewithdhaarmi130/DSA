# Find missing number using sum formula

arr = [1, 2, 4, 5]

n = 5  # total numbers from 1 to n

total_sum = n * (n + 1) // 2
array_sum = sum(arr)

missing = total_sum - array_sum

print("Missing number:", missing)
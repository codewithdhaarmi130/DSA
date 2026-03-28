# Find maximum consecutive 1s

arr = [1, 1, 0, 1, 1, 1]

count = 0
max_count = 0

for num in arr:
    if num == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Maximum consecutive 1s:", max_count)
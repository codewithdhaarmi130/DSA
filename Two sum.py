# Two Sum using hash map

arr = [2, 7, 11, 15]
target = 9

num_map = {}

for i in range(len(arr)):
    complement = target - arr[i]
    
    if complement in num_map:
        print("Indices:", num_map[complement], i)
        break
    
    num_map[arr[i]] = i
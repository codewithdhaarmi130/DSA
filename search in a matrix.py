# Search in a matrix

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = int(input("Enter target: "))

rows = len(matrix)
cols = len(matrix[0])

low = 0
high = rows * cols - 1

while low <= high:
    mid = (low + high) // 2

    # Convert 1D index to 2D
    r = mid // cols
    c = mid % cols

    if matrix[r][c] == target:
        print("Element Found")
        break
    elif matrix[r][c] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element Not Found")
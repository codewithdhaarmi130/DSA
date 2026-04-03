# Set matrix zero

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows = len(matrix)
cols = len(matrix[0])

row_zero = set()
col_zero = set()

# Step 1: Find zero positions
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_zero.add(i)
            col_zero.add(j)

# Step 2: Set rows and columns to zero
for i in range(rows):
    for j in range(cols):
        if i in row_zero or j in col_zero:
            matrix[i][j] = 0

# Print result
for row in matrix:
    print(row)
def is_diagonal_matrix(matrix, r):
    for i in range(r):
        for j in range(r):
            if i != j and matrix[i][j] != 0:
                return 0
    return 1

# Read input
r = int(input())
matrix = []
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check if the matrix is diagonal and print the result
print(is_diagonal_matrix(matrix, r),end="")

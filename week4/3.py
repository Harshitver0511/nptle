def is_symmetric_matrix(matrix, r):
    for i in range(r):
        for j in range(r):
            if matrix[i][j] != matrix[j][i]:
                return 0
    return 1

# Read input
r = int(input())
matrix = [list(map(int, input().split())) for _ in range(r)]

# Check if the matrix is symmetric and print the result
print(is_symmetric_matrix(matrix, r),end="")

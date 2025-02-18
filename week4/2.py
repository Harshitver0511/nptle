def add_transpose_by_scalar(matrix, r, c, s):
    # Compute the transpose and add scalar
    result = [[matrix[j][i] + s for j in range(r)] for i in range(c)]
    return result

# Read input
r = int(input())
c = int(input())
matrix = [list(map(int, input().split())) for _ in range(r)]
s = int(input())

# Compute and print the result
result = add_transpose_by_scalar(matrix, r, c, s)
for i, row in enumerate(result):
    print(" ".join(map(str, row)), end="\n" if i < len(result) - 1 else "")

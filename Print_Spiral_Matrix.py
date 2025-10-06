def spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    val = 1
    left, right, top, bottom = 0, n-1, 0, n-1

    while left <= right and top <= bottom:
        for i in range(left, right+1):
            matrix[top][i] = val
            val += 1
        top += 1
        for i in range(top, bottom+1):
            matrix[i][right] = val
            val += 1
        right -= 1
        for i in range(right, left-1, -1):
            matrix[bottom][i] = val
            val += 1
        bottom -= 1
        for i in range(bottom, top-1, -1):
            matrix[i][left] = val
            val += 1
        left += 1
    for row in matrix:
        print(row)

spiral_matrix(4)

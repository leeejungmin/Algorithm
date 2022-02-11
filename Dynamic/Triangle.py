triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
triangle = [[0]+t+[0] for t in triangle]


print(triangle[-1])

    for row in len(triangle):
        if col == 0:
            triangle[row][col] = triangle[row][col] + triangle[row-1][col]
        elif col == len(triangle):
            triangle[row][col] = triangle[row][col] + triangle[row-1][col-1]
        else:
            triangle[row][col] += max(triangle[row-1][col-1],triangle[row-1][col])

    return max(triangle[-1])

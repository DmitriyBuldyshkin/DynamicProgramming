def grid_trav(m, n):
    """
    O(m * n) time
    O(m * n) space
    """
    table = [[0] * (n+1) for i in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i + 1 <= m:
                table[i+1][j] += table[i][j]
            if j + 1 <= n:
                table[i][j+1] += table[i][j]

    return table[m][n]


print(grid_trav(1, 1))
print(grid_trav(2, 3))
print(grid_trav(3, 2))
print(grid_trav(3, 3))
print(grid_trav(18, 18))

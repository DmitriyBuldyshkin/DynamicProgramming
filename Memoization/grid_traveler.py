# You can either go down or right inside a grid
def grid_trav(row, col):
    """
    O(2^(row + col)) time
    O(row + col) space
    """

    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0

    return grid_trav(row - 1, col) + grid_trav(row, col - 1)


# print(grid_trav(1, 1))
# print(grid_trav(2, 3))
# print(grid_trav(3, 2))
# print(grid_trav(3, 3))


# Memoization
def grid_trav_modified(row, col, memo=None):
    """
    O(row * col) time
    O(row + col) space
    """
    
    if memo is None:
        memo = {}
    key = f"{row}, {col}"

    # are the arguments inside memo?
    if key in memo:
        return memo[key]

    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0

    ans = grid_trav_modified(row - 1, col, memo) + grid_trav_modified(row, col - 1, memo)  # adding arguments in memo
    memo[key] = ans
    return ans


print(grid_trav_modified(1, 1))
print(grid_trav_modified(2, 3))
print(grid_trav_modified(3, 2))
print(grid_trav_modified(3, 3))
print(grid_trav_modified(18, 18))

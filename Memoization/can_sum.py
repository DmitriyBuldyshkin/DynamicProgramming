def can_sum(target, numbers):
    """
    O(n ^ m) time
    O(m) space

    m = target
    n = list/array length
    """
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers):
            return True

    return False


# print(can_sum(7, [2, 3]))
# print(can_sum(7, [5, 3, 4, 7]))
# print(can_sum(7, [2, 4]))
# print(can_sum(8, [2, 3, 5]))


# Memoization
def can_sum_modified(target, numbers, memo=None):
    """
    O(m * n) time
    O(m) space

    m = target
    n = list/array length
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum_modified(remainder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


print(can_sum_modified(7, [2, 3]))
print(can_sum_modified(7, [5, 3, 4, 7]))
print(can_sum_modified(7, [2, 4]))
print(can_sum_modified(8, [2, 3, 5]))
print(can_sum_modified(300, [7, 14]))

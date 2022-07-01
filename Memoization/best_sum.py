def best_sum(target, numbers):
    """
    O(n ^ m) time
    O(m ^ 2) space

    m = target
    n = list/array length
    """
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        combination = best_sum(remainder, numbers)
        if combination is not None:
            combination.append(num)
            # if the current combination is shorter than shortest, update it
            if shortest_combination is None:
                shortest_combination = combination
            elif len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination


# print(best_sum(7, [5, 3, 4, 7]))
# print(best_sum(8, [2, 3, 5]))
# print(best_sum(8, [1, 4, 5]))


# Memoization
def best_sum_modified(target, numbers, memo=None):
    """
    O(n * m ^ 2) time
    O(m ^ 2) space

    m = target
    n = list/array length
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        combination = best_sum_modified(remainder, numbers, memo)
        if combination is not None:
            combination_copy = combination.copy()
            combination_copy.append(num)
            if shortest_combination is None or len(combination_copy) < len(shortest_combination):
                shortest_combination = combination_copy

    memo[target] = shortest_combination
    return shortest_combination


print(best_sum_modified(7, [5, 3, 4, 7]))
print(best_sum_modified(8, [2, 3, 5]))
print(best_sum_modified(8, [1, 4, 5]))
print(best_sum_modified(100, [1, 2, 5, 25]))

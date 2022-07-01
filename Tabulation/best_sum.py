def best_sum(target, numbers):
    """
    O(m * n) time
    O(m ^ 2) space

    m = target
    n = len(numbers)
    """
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    combination = [num] + [num for num in table[i]]
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination

    return table[target]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))


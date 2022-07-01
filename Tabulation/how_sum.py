def how_sum(target, numbers):
    """
    O(m * n) time
    O(m ^ 2) space

    m = target
    n = len(numbers)
    """
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = [num] + [num for num in table[i]]

    return table[target]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))

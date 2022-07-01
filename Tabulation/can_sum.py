def can_sum(target, numbers):
    """
    O(m * n) time
    O(m) space

    m = target
    n = len(numbers)
    """
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target + 1):
        for num in numbers:
            if table[i] and i + num <= target:
                table[i + num] = True

    return table[target]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))

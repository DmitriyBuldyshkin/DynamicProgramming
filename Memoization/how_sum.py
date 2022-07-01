def how_sum(target, numbers):
    """
    O(n ^ m) time
    O(m) space

    m = target
    n = list/array length
    """
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        result = how_sum(remainder, numbers)
        if result is not None:
            result.append(num)
            return result

    return None


# print(how_sum(7, [2, 3]))
# print(how_sum(7, [5, 3, 4, 7]))
# print(how_sum(7, [2, 4]))
# print(how_sum(8, [2, 3, 5]))


def how_sum_modified(target, numbers, memo=None):
    """
    O(n * m) time
    O(m) space

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

    for num in numbers:
        remainder = target - num
        result = how_sum_modified(remainder, numbers, memo)
        if result is not None:
            result.append(num)
            memo[target] = result
            return result

    memo[target] = None
    return None


print(how_sum_modified(7, [2, 3]))
print(how_sum_modified(7, [5, 3, 4, 7]))
print(how_sum_modified(7, [2, 4]))
print(how_sum_modified(8, [2, 3, 5]))
print(how_sum_modified(300, [7, 14]))

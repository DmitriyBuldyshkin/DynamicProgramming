def fib(num):
    """
    O(2^n) time
    O(n) space
    """

    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)


# print(fib(6))
# print(fib(7))
# print(fib(8))


# Memoization
def fib_modified(num, memo=None):
    """
    O(n) time
    O(n) space
    """

    if memo is None:
        memo = {}

    # is the number inside memo?
    if num in memo:
        return memo[num]
    if num <= 2:
        return 1

    memo[num] = fib_modified(num - 1) + fib_modified(num - 2)  # adding new numbers in memo
    return memo[num]


print(fib_modified(6))
print(fib_modified(7))
print(fib_modified(8))
print(fib_modified(30))

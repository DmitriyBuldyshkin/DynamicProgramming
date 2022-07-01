def count_construct(target, word_bank):
    """
    O(n ^ m * m) time
    O(m ^ 2) space

    m = len(target)
    n = len(word_bank)
    """
    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.find(word) == 0:
            num_ways = count_construct(target[len(word):], word_bank)
            total_count += num_ways

    return total_count


# print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))


# Memoization
def count_construct_modified(target, word_bank, memo=None):
    """
    O(n * m ^ 2) time
    O(m ^ 2) space

    m = len(target)
    n = len(word_bank)
    """
    if memo is None:
        memo = {}

    total_count = 0

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    for word in word_bank:
        if target.find(word) == 0:
            num_ways = count_construct_modified(target[len(word):], word_bank, memo)
            total_count += num_ways

    memo[target] = total_count
    return total_count


print(count_construct_modified("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct_modified("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct_modified("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct_modified("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_modified("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
"e"
"ee",
"еее"
"eeee"
"eeeee"
"ееееее",
]))

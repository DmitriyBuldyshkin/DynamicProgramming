def can_construct(target, word_bank):
    """
    O(n ^ m * m) time
    O(m ^ 2) space

    m = len(target)
    n = len(word_bank)
    """
    if target == "":
        return True

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank) is True:
                return True

    return False


# print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

# Memoization
def can_construct_modified(target, word_bank, memo=None):
    """
    O(n * m ^ 2) time
    O(m ^ 2) space

    m = len(target)
    n = len(word_bank)
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct_modified(suffix, word_bank, memo) is True:
                memo[target] = True
                return True

    memo[target] = False
    return False


print(can_construct_modified("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_modified("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_modified("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_modified("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
"e"
"ee",
"еее"
"eeee"
"eeeee"
"ееееее",
]))

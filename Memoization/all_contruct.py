def all_construct(target, word_bank):
    if target == "":
        return [[]]

    result = []
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            for way in suffix_ways:
                way = [word] + way
                result.append(way)

    return result


# print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

"""
Both are:
    O(n ^ m) time
    O(m) space

m = len(target)
n = len(word_bank)
"""


# Memoization
def all_construct_modified(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct_modified(suffix, word_bank, memo)
            for way in suffix_ways:
                way = [word] + way
                result.append(way)

    memo[target] = result
    return result


print(all_construct_modified("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct_modified("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct_modified("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct_modified("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

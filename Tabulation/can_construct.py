def can_construct(target, word_bank):
    """
    O(m ^ 2 * n) time
    O(m) space

    m = len(target)
    n = len(word_bank)
    """
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True

    return table[len(target)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
"e"
"ee",
"еее"
"eeee"
"eeeee"
"ееееее",
]))

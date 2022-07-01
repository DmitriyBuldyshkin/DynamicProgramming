def all_construct(target, word_bank):
    """
    O(n ^ m) time
    O(n ^ m) space

    m = len(target)
    n = len(word_bank)
    """
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                for el in table[i]:
                    temp = el[:]
                    temp.append(word)
                    table[i + len(word)].append(temp[:])

    return table[len(target)]


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

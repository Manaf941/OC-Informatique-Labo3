def is_palindrome(word: str):
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[-i - 1]:
            return False

    return True

for word in [ "radar", "excès", "ressasser" ]:
    print(word, is_palindrome(word))
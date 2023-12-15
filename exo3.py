vowels = set("aeiouy")

def extract_vowels(word: str):
    count = 0
    for char in word:
        if char not in vowels:
            continue

        count += 1

    return count

for word in ["aujourd'hui", "exceptionnel", "cygne"]:
    print(word, extract_vowels(word))

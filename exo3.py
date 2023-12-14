vowels = list("aeiouy")

def extract_vowels(word: str):
    result = ""
    for char in word:
        if char not in vowels:
            continue

        result += char

    return result

print(extract_vowels("aujourd'hui")) # auouui
print(extract_vowels("exceptionnel")) # eeioe
print(extract_vowels("cygne")) # ye

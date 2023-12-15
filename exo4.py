from typing import List

def remove_repetitions(l: List[str]):
    # set is not deterministic
    # and i'm not sure i'm allowed to use it
    # return list(set(l))
    result = []
    for elem in l:
        if elem in result:
            continue
        result.append(elem)

    return result

print("a)", remove_repetitions(
    ["Lausanne", "Fribourg", "Genève", "Berne", "Lausanne", "Zurich", "Lausanne"]
))
print("b)", remove_repetitions(
    ["Lausanne", "Fribourg", "Genève", "Berne", "Lausanne", "Zurich", "Lausanne", "Berne", "Genève", "Lausanne", "Zurich"]
))
from typing import List

def remove_repetitions(l: List[str]):
    return list(set(l))

print("a)", remove_repetitions(
    ["Lausanne", "Fribourg", "Genève", "Berne", "Lausanne", "Zurich", "Lausanne"]
))
print("b)", remove_repetitions(
    ["Lausanne", "Fribourg", "Genève", "Berne", "Lausanne", "Zurich", "Lausanne", "Berne", "Genève", "Lausanne", "Zurich"]
))
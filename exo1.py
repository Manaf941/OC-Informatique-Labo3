from typing import List

notes_français = [3, 4.5, 5.5, 3.5, 2.5, 4]

# Ajouter la note 5 en position 4
notes_français.insert(3, 5)

# Ajouter la note 3.5 en fin de liste
notes_français.append(3.5)

# Supprimer le premier 3
notes_français.remove(3)

def moyenne(notes: List):
    somme = 0
    for note in notes:
        somme += note

    return somme / len(notes)

def arrondir(note):
    error = note % 0.5
    note = note - error
    if error >= 0.25:
        note += 0.5

    return note

# 4.071428571428571, la fonction est correcte
# print(moyenne(notes_français))

notes_maths = [4, 4.5, 5, 2, 3.5]
notes_allemand = [2, 5, 2.5, 4.5, 3.5, 4]
notes_anglais = [5, 4.5, 5, 5.5, 4.5, 5]
notes_os = [5, 4.5, 4.5, 5, 5.5]

notes = {
    "français": notes_français, # 4
    "maths": notes_maths, # 4
    "allemand": notes_allemand, # 3.5
    "anglais": notes_anglais, # 5
    "os": notes_os # 5
}

panier = 0
for matiere in notes:
    moy = arrondir(moyenne(
        notes[matiere]
    ))
    print(f"{matiere}: {moy}")
    
    if matiere == "allemand" or matiere == "anglais":
        panier += moy/2
    else:
        panier += moy

print(f"Panier: {arrondir(panier)}")

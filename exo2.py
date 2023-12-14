powers = []

maxpower = 14
minpower = 1
for n in range(minpower, maxpower + 1):
    powers.append(2**n)

print(powers, f"Nb: {len(powers)}")
print(f"2048 se trouve à l'index: {powers.index(2048)}")

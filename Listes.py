# extrait toutes les notes supérieures à la moyenne et les stocke dans une nouvelle liste.
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

sum = 0
nb = len(notes)
for i in range(nb):
    sum += notes[i]

moy = sum / nb
print(moy)

# Challenge 2 : Les mots communs

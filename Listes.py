# extrait toutes les notes supérieures à la moyenne et les stocke dans une nouvelle liste.
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

sum = 0
nb = len(notes)
for i in range(nb):
    sum += notes[i]

moy = sum / nb
print(moy)

# regrouper dans une liste les mots communs entre deux chaînes de caractères Ch1 et Ch2.
Ch1 = "test AAmir Python AAAmer "
Ch2 = "Python mots communs entre "

mots1 = Ch1.split()
mots2 = Ch2.split()

communs = []
for mot1 in mots1:
    for mot2 in mots2:
        if mot1 == mot2 and mot1 not in communs:
            communs.append(mot1)

print(communs)

# Challenge 3 : Manipulation et tri de listes mixtes

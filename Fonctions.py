import math
#	Challenge 1 : Présentation personnalisé



def horaire_sup(nom: str, salaire_horaire: float, nb_heures: int) -> float:
    salaire_total = nb_heures * salaire_horaire

    if nb_heures > 40:
        heures_sup = nb_heures - 40
        salaire_total = 40 * salaire_horaire + heures_sup * salaire_horaire * 1.5

    return salaire_total


horaire_sup("aamir",22.2,12)    


# Challenge 2 : Fonction calculation() – somme et différence

def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference

# Challenge 3 : Mini-projets algorithmiques regroupés

# factorielle 

def factorielle(nb):
    result = 1
    for i in range(1, nb + 1):
        result *= i
    return result

# table de multiplication

def TableMultiplication(m):
    resultat = []
    for i in range(1,10):
     resultat.append(m*i);
    return resultat

print(TableMultiplication(5))

# carré parfait.

def perfectCube(N):
    number = math.isqrt(N)
    if(number**2 == N):
        return 1
    else :
        return 0
perfectCube(16)

# afficher chaque caractère un par un.
def affichageChar(char):
 i=0
 for i in range(0,len(char)):
    print(char[i])

affichageChar("dndks")




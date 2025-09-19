#  Transformer une liste imbriquée avec une fonction récursive.
list2 =[2,2,4,9,8,3]
#  map 
resultat = list(map(lambda num:num*num,list2))
print(resultat)

# filter 

filter_resultat = list(filter(lambda number:number <5,list2))

print(filter_resultat)


# Challenge 2 : Transformation Avancée de Données

mixed_list = [2,3,-4,9,-6,8]

get_number_positive = list(filter(lambda number : number>0,mixed_list))
get_cub_nb = list(map(lambda number : number*number,get_number_positive))

get_sorted_nb = list(sorted(get_cub_nb))
print(get_sorted_nb)

# Challenge 3 : Tri personnalisé avec clé dynamique
list_etudiant = [{'nom': 'Aamie', 'note': 12}, {'nom': 'Aadkde', 'note': 21}]
trier_etudiants = list(sorted(list_etudiant, key=lambda number:number["note"],reverse=True) and filter(lambda student: student["note"] > 0, list_etudiant))

print(trier_etudiants)

# Challenge 4 : Fusion intelligente de listes

listenb1 = [1,7,8,9,5,95]
listenb2 =[23,3,83,54]
def sortedListe(list33):
    return list(sorted(list33))
def  fusionner_listes(list11,list2):
    list11 = list11.extend(list2)
    remove_Redoublant = list(set(list11))
    return sortedListe(remove_Redoublant)
    
fusionner_listes(listenb1,listenb2)

# Challenge 5 : Partitionnement de liste

def paire(listez):
    return list(filter(lambda number : number %2 ==0),listez)
def impaire(listez):
    return list(filter(lambda number : number %2 !=0),listez)
globalListe  = listenb1.append(listenb2)
get_paire = paire(globalListe)
get_impaire = impaire(globalListe)
def tupleFunction(listpaire,listimpaire):
    return tuple(listimpaire,listpaire)

tupleFunction(get_paire,get_impaire)    

# Challenge 6 : Réduction avec accumulation personnalisée
from functools import reduce
nums = [4,5,6,9]

reduire_liste =  reduce(lambda number1,number2 : number1+number2,nums)

print(reduire_liste)

# Challenge 7 : Transformation imbriquée
listCh7 = [1, [2, 3, [4, 5]], 6]

for i in range(len(listCh7)):
    if(isinstance(listCh7[i],(list))):
        for j in range(listCh7[i]):
           list22+= list(map(lambda num:num*num,listCh7[i]))
    else:
           list2+= list(map(lambda num:num*num,listCh7[i])) 
  
globalList= list2,list2    

print(globalList)

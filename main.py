from .Exeption  import STRExeptionHandler
# # 	Challenge 1 : Présentation personnalisée 

get_prenom = input("donner moi votre nom")
get_age = str(input("donner moi votre age "))

print("votre age est " + get_age + " votre nom est " + get_prenom)

# #Challenge 2 : Calcul de salaire avec heures supplémentaires

get_nom = str(input("donner moi votre nom :"))
get_salaire_horaire = float(input("donner moi votre  salaire horaire :"))
nb_heures =  int(input("donner moi votre  nombre d heures :"))

salaire_total =nb_heures * get_salaire_horaire

if(nb_heures > 40):
    revenue = nb_heures-40 * 1.5
    salaire_total += 40 * float(get_salaire_horaire) + revenue

print("votre saliare total is" , float(salaire_total))

#Challenge 3 : Gestion des erreurs utilisateur

get_nom = str(input("donner moi votre nom :"))
if(get_age is not str):
     
    #  j ai ajouter la class a Exeption file 
     raise STRExeptionHandler;
try:
    get_salaire_horaire = float(input("donner moi votre  salaire horaire :"))
except ValueError:
        print("votre numero not valide & must be int ")    
try:
        nb_heures = int(input("donner moi votre  nombre d heures :"))
except ValueError:  
    print("votre numero not valide & must be float ") 

salaire_total = nb_heures * get_salaire_horaire

if nb_heures > 40:
 revenue = (nb_heures - 40) * get_salaire_horaire * 1.5
salaire_total = 40 * get_salaire_horaire + revenue

print("votre saliare total is", float(salaire_total))
    

# Challenge 4 : Déterminer le signe d’un produit de deux nombres

get_nembre1 = float(input("donner moi  le premier nombre : "))
get_nember2 = float(input("donner moi  le 2 eme nombre : "))
produit = get_nembre1 * get_nember2

if produit > 0:
    print("Le produit est positif.")
elif produit < 0:
    print("Le produit est négatif.")
else:
    print("Le produit est nul.")


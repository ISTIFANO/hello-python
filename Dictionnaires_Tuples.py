First_dict = { "Appareil": "Laptop", "Marque": "IBM",
               "Carte mère": "MSI Z490",
                 "Carte Graphique":"GeForce RTX 3070", 
                 "RAM": "16G", "Processeur": "Intel core i7-G11",
                   "SSD": "1 To" }

# Challenge 1 : Manipulation des dictionnaires Python
#  Parti 1: 
# first methode  

First_dict["RAM"]="32G"

# 2 methode 
for cle, value in First_dict.items():
    if cle == "RAM":
        First_dict[cle] = "32G"

print(First_dict)

# Afficher successivement :

print(First_dict)

# La liste des clés du dictionnaire

for cle, value in First_dict.items():
    
    print(cle)

# La liste des valeurs

for cle, value in First_dict.items():
    
    print(value)

# La liste des paires clé-valeur
for cle, value in First_dict.items():
    print({cle : value})
    
# Inverser les paires "Processeur" : "Intel core i7-G11" et "Carte Graphique" : "GeForce RTX 3070"

for cle, value in First_dict.items():
     if(cle == "Processeur" or cle == "Carte Graphique") :
         First_dict["Processeur"]="Intel core i7-G11"
         First_dict["Carte Graphique"]="GeForce RTX 3070"
         
First_dict["Processeur"], First_dict["Carte Graphique"] = First_dict["Carte Graphique"], First_dict["Processeur"]

print(First_dict)

# Ajouter la paire clé-valeur suivante : "Système d’exploitation": "Windows 10"

First_dict["Système d’exploitation"] = "Windows 10"

#Parti 2: 
notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
somme = 0
for cle, value in notes_eleves.items():
    somme += value
moyenne = somme / len(notes_eleves)

print(moyenne)
# les étudiants admis et les valeurs des clés sont les moyennes obtenues

for cle, value in notes_eleves.items():
    if(value >10):
      print(cle)


# les étudiants non admis et les valeurs des clés sont les moyennes obtenues

for cle, value in notes_eleves.items():
    if(value <10):
      print(cle)

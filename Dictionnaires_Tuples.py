First_dict = { "Appareil": "Laptop", "Marque": "IBM",
               "Carte mère": "MSI Z490",
                 "Carte Graphique":"GeForce RTX 3070", 
                 "RAM": "16G", "Processeur": "Intel core i7-G11",
                   "SSD": "1 To" }

# Challenge 1 : Manipulation des dictionnaires Python
 
# first methode  

First_dict["RAM"]="32G"

# 2 methode 
for cle, value in First_dict.items():
    if cle == "RAM":
        First_dict[cle] = "32G"

print(First_dict)

# Afficher successivement :



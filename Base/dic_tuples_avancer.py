# Challenge 1 : Fusion de dictionnaires avec mise à jour personnalisée
dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 3, 'z': 4}

def fusionner_dicts(d1, d2, fonction):
    resultat = {}
    for cle, valeur in d1.items():
        resultat.setdefault(cle, valeur)
    for cle, valeur in d2.items():
        if cle in resultat:
            resultat[cle] = fonction(resultat[cle], valeur)
        else:
            resultat.setdefault(cle, valeur)
    return resultat

print(fusionner_dicts(dict_a, dict_b, lambda a, b: a + b))


# Challenge 2 : Filtrage d’un dictionnaire
def filtrer_dict(dictionnaire: dict, fonction):
    items = list(dictionnaire.items())
    print("Items origine :", items)
    dict_filtre = dict(filter(lambda elem: fonction(elem[1]), items))
    print("Dictionnaire filtre :", dict_filtre)

dict_test = {'p': 5, 'q': 12, 'r': 8, 's': 15}
filtrer_dict(dict_test, lambda val: val > 10)


# Challenge 3 : Création de tuples à partir de dictionnaires
def dict_vers_tuples(dictionnaire, fonction):
    items = list(dictionnaire.items())
    tri = sorted(items, key=fonction)
    print("Tri :", tri)
notes = {'math': 10, 'physique': 5, 'chimie': 15}
dict_vers_tuples(notes, lambda item: item[1])


# Challenge 4 : Regroupement par clé dans un dictionnaire
def regrouper_par_cle(paires):
    resultat = {}
    for cle, valeur in paires: 
        if cle not in resultat: 
            resultat[cle] = []       
        resultat[cle].append(valeur)      
    return resultat

paires = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
print(regrouper_par_cle(paires))


# Challenge 5 : Transformation de tuples avec fonction
def transformer_tuples(liste_tuples, fonction):
    resultat = []
    for tup in liste_tuples:
        nouveau_tup = tuple(map(fonction, tup))  
        resultat.append(nouveau_tup)         
    return resultat

tuples_initiaux = [(1, 2), (3, 4)]
print(transformer_tuples(tuples_initiaux, lambda n: n * 2))


# Challenge 6 : Dictionnaire imbriqué à plat
def aplatir_dict(dictionnaire, prefixe=''):
    resultat = []
    for cle, valeur in dictionnaire.items():
        newCle = f"{prefixe}.{cle}" if prefixe else cle
        if isinstance(valeur, dict):
            resultat += aplatir_dict(valeur, newCle)
        else:
            resultat.append((newCle, valeur))
    return resultat

dict_imbr = {'a': 1, 'b': {'c': 2, 'd': 3}}
print(aplatir_dict(dict_imbr))



def functifontUPPLE(dic, crit):
    tuple = tuple(dec.items)

    return sorted(tuple,key=crit)

crit01 = lambda x : x[0]
crit02 = lambda x : x[1]
dec={"Aamie":12}
functifontUPPLE(dec,crit01)


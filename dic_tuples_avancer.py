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

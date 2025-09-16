#	Challenge 1 : Présentation personnalisé



def horaire_sup(nom: str, salaire_horaire: float, nb_heures: int) -> float:
    salaire_total = nb_heures * salaire_horaire

    if nb_heures > 40:
        heures_sup = nb_heures - 40
        salaire_total = 40 * salaire_horaire + heures_sup * salaire_horaire * 1.5

    return salaire_total


horaire_sup("aamir",22.2,12)    


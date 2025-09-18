from .Etudiant  import Etudiant
from .Enseignant  import Enseignant
class Ecole:
       
     def __init__(self,nom,liste_etudiants:Etudiant,liste_enseignants:Enseignant):
              self.nom =nom
              self.liste_etudiants=liste_etudiants
              self.liste_enseignants =liste_enseignants
              pass
     
     def ajouter_etudiant(self,etudiants:Etudiant):
            list=[]
            list.append(etudiants)
            return list
     def  ajouter_enseignant(enseignant:Enseignant):
            list_enseignant=[]
            list_enseignant.append(enseignant)
            return list_enseignant
     
     def afficher_tous_les_membres(self):
        infos = "liste des etudiants :\n"
        for etudiant in self.liste_etudiants:
            infos += etudiant.afficher_infos() + "\n"
        infos += "\nliste des enseignants :\n"
        for enseignant in self.liste_enseignants:
            infos += enseignant.afficher_infos() + "\n"
        return infos  


            
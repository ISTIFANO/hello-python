from abc import ABC, abstractmethod
class  Personne(ABC) :
    def __init__(self,nom,prenom,age):
            self.nom = nom
            self.prenom = prenom
            self.age = age
            pass
    @abstractmethod
    def afficher_infos(self):
         pass
    def __str__(self):
           return " votre nom : "+self.nom + " votre prenom :" + self.prenom +" votre age : " +self.age

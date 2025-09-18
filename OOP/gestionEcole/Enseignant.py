from .Personne  import Personne
from abc import ABC, abstractmethod

class Enseignant(Personne):
       
        def __init__(self, nom, prenom, age,specialite,salaire ):
              super().__init__(nom, prenom, age)
              self.specialite=specialite
              self.c =salaire
              pass
            
        @property
        def afficher_infos(self):
              return super.__str__ +"this is mat : "+{self.specialite}+"this is notes "+{self.salaire}
        @property
        def salaire(self):
               return self.salaire
        @property.setter
        def salaire(self,salaire):
               if(salaire<0):
                      return"salaire must be positive "
               else:
                      return self.salaire + salaire
        @property
        def specialite(self):
               return self.specialite
        @property.setter
        def specialite(self,specialite):
    
                      return self.specialite + specialite  
from .Personne  import Personne
from abc import ABC, abstractmethod

class Etudiant(Personne):
       
        def __init__(self, nom, prenom, age,matricule,notes=[] ):
              super().__init__(nom, prenom, age)
              self.matricule =matricule
              self.notes=notes
              pass
            
        @property
        def afficher_infos(self):
              return super.__str__ +"this is mat : "+{self.matricule}+"this is notes "+{self.notes}
              
        def ajouter_note(self,note):
               self.notes+=note
               return self.notes
        def moyenne(self):
               for i in range(len(self.notes)):
                      sum+=self.notes[i]
               return sum/len(self.notes)
      
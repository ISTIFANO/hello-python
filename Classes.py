# Challenge 1 : Gestion d’un compte bancaire en POO
class CompteBancaire:

        def __init__(self,nom_proprietaire,solde):
                self.nom_proprietaire = nom_proprietaire 
                self.solde = solde

        def deposer(self,montant):
                self.solde += montant
                return self.nom_proprietaire +"votre solde est : ", self.solde

        def retirer(self,montant):
                try:
                    if(self.solde<montant):
                                print("vous n avez pas un solde valide ")
                    else:
                            self.solde -= montant
                            return self.nom_proprietaire + "votre solde est : ", self.solde
                except Exception as error:
                        print(error)    

                        def afficher_solde(self):
                                return "votre solde est : " + self.nom_proprietaire + "votre solde est : ", self.solde
                                            

# Challenge 2 : Système de gestion d’école
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


            
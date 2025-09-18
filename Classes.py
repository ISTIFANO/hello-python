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



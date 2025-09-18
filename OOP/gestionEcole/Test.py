from Etudiant  import Etudiant

from Enseignant  import Enseignant




etudiant = Etudiant("Aamir","El Amiri",22,"matimaticien",[23,233,23])
enseinant =  Enseignant("tayeb","souini",30,"developper java&angular",14000)

print(enseinant.afficher_infos())
print(etudiant.afficher_infos())
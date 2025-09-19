# from Etudiant  import Etudiant

# from Enseignant  import Enseignant
import os




# etudiant = Etudiant("Aamir","El Amiri",22,"matimaticien",[23,233,23])
# enseinant =  Enseignant("tayeb","souini",30,"developper java&angular",14000)

# print(enseinant.afficher_infos())
# print(etudiant.afficher_infos())

path ="./devAi2eme"
file_name ="devAi"
 
try:

    os.mkdir("devAi2eme")
    files = os.scandir(path)
    c={}
    for file in files:
             globalpath =os.path.join(path,file)
             with  open("globalpath","w") as fileName:
                fileName.write("test")
                fileName.write("El  amiri")
                fileR = open(globalpath,"r")
                c+=fileR
finally:
        fileName.close()
        fileR.close()


  
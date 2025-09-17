import os
# docs 
try:
    with open("file.txt", "w") as file:
        file.write("Hello")
        file.write("Aamir El amiri")

    print(" successfully")


    with open("file.txt", "r") as file:
        content= file.read()
    print(content)
finally:
    file.close()

    # Challenge 1 : Extraction et Traitement de Fichiers

import os

path = "./Files"
files = os.listdir(path)  
print("fichiers :", files)
content = ""

for filename in files:
    full_path = os.path.join(path, filename)  
    with open(full_path, "r") as file:
        content += file.read() + "\n" 

print(content)

# Challenge 2 : Recherche de Fichiers
# methode 1
# with os.scandir(path) as allfiles:
#     for langue in allfiles:
#         print(langue)
#         if langue.is_file():
#             if (langue=="java.txt"):
#                 print("FILE EXIST")

# methode 2
if(os.path.exists(path)):
    print("file exist")
else:
    print("file note exist ")
         
#  Création de Répertoires
    try:
        os.mkdir("langues")
        
        print("folder has been created succ")
    except FileExistsError:
            print("Directory already exists.")
    except Exception as Error:
        print(Error)
#  Création de Répertoires
    try:
        folderName="C:/Users/aamir/Desktop/YC/Python/hello-python/langues"
        file = os.mkdir(folderName)
        if(os.path.dirname(folderName)):
            get_file = open(folderName+"/Repertoires.txt","w")
            get_file.write("this is a Repertoires file ")
            get_file.close()
        print("folder has been created succ")
    except FileExistsError:
            print("Directory already exists.")
    except Exception as Error:
        print(Error)

        # Challenge 5 : Copie Sélective de Fichiers

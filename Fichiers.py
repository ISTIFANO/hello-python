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
        folderName="langues3"
        file = os.mkdir(folderName)
        if(os.path.dirname(folderName)):
            get_file = open(folderName+"/Repertoires.txt","w")
            get_file.write("this is a Repertoires file ")
            get_file.close()
        print("file has been created succ")
    except FileExistsError:
            print("Directory already exists.")
    except Exception as Error:
        print(Error)

        # Challenge 5 : Copie Sélective de Fichiers
        try:
            folder="files01"
            createFolder=os.mkdir(folder)
            if(os.path.dirname(folder)):
                 getfile = open(folderName+"Test.txt","w")
                 getfile.write('this is all you to be ai developer ')
                 getfile.close()
        except Exception as error:
             print(error)            

             
               # Challenge 5 : Copie Sélective de Fichiers
lists = ["Hello Aamie" , "HelloAA", "heelo"]
with open(path+"/Filles/test.txt" , "w") as f :
    for i in lists :
        print(i) 
        k = i 
        f.write(f"{i}\n")
enregistred = 0 
with open(path+"/Filles/test.txt" , "r") as f :
    lines = f.readlines()
    for i in lists :
        i = i
        if i in lines :
            enregistred +=1 
print(enregistred)
if enregistred == len(lists) : 
    print("the data saved correctly")   

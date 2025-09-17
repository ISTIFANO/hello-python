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



#El codi per fer un log-in i registrarse al projecte de Python del Jofre i l'Ivan

nom = input("Digui el seu nom/usuari: ")
contra = input("Digui la seva contrasenya: ")

fitxer = open("usuaris/usuaris.txt", "r")
nom_login = "."

login = False 
while nom_login:
    nom_login = fitxer.readline()
    contra_login = fitxer.readline()

    if nom_login == nom + "\n" and contra_login == contra + "\n":
        login = True
        fitxer.close()
        break


if login == True:
    print("Log in correcte, benvingut.")

else: 
    fitxer = open("usuaris/usuaris.txt", "a")
    print("Registra't: ")
    fitxer.write("\n" + input("Digui el seu nom: "))
    fitxer.write("\n" + input("Digui la seva contrasenya: ")) + "\n" + "\n"


        
        


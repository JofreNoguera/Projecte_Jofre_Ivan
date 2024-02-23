#El codi del projecte del Jofre i l'Ivan

import tkinter as tk


def registrar_usuario(nom_login):
    # Crear un archivo con el nombre del usuario
    nombre_archivo = f"{nom_login}.txt"
    with open(f"perfils/{nombre_archivo}", "w") as archivo:
        archivo.write("Informació de l'usuari:\n")
        archivo.write(f"Nombre de usuario: {nom_login}\n")
        archivo.write(f"Ciutat: {ciutat}\n")
        

        # Puedes agregar más información del usuario aquí si lo deseas

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
    ciutat = input("Digui de quina ciutat/poble es vosté: ")
    registrar_usuario(nom)


else: 
    fitxer = open("usuaris/usuaris.txt", "a")
    print("Registra't: ")
    nom_login = fitxer.write("\n" + "\n" + input("Digui el seu nom:\n "))
    contra_login = fitxer.write("\n" + input("Digui la seva contrasenya:\n ") + "\n")
    ciutat = input("Digui de quina ciutat/poble es vosté: ")
    registrar_usuario(nom)


import requests  # Importa la biblioteca requests para realizar solicitudes HTTP



#import requests
API_Key = "d206fdab52fec3ab264e1f0d49aa16ba"

#once we create the GUI we will replace the city input:
city = input("Escrigui la ciutat o poble del qual vol obtenir el temps: ")
Base_url = "http://api.openweathermap.org/data/2.5/weather"

#Creating the full URL 
request_url = f"{Base_url}?appid={API_Key}&q={city}"
#URL completa = http://api.openweathermap.org/data/2.5/weather?appid=d206fdab52fec3ab264e1f0d49aa16ba&q=spain"

# we'll store the response code here in get_weather
get_weather = requests.get(request_url)

#extracting the Json file
if get_weather.status_code == 200:
    data = get_weather.json()
    weather_unscripted = data
    #we check what information we get from the json file. 
    

#weather
    weather = data['weather'][0]['description']
#temperature (converting it to Celsius)
    temp = round(data['main']['temp'] - 273.15, 2)
   # temp_e = print(f"La temperatura és de: {temp}ºC, la qual es {(temp * 9 / 5) + 32 }ºF")
#Feels Like (converting it to Celsius)
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    
#Humidity
    Humid = data['main']['humidity']

#Wind Speed
    Wind = data['wind']['speed']
  #  Wind_e = print(f"La velocitat del vent és de: {Wind}m/s")



# Iniciar el bucle de eventos
ventana = tk.Tk()
ventana.title("Projecte Python 2023-2024 | Jofre i Ivan")
Ciutat_e = tk.Label(ventana, text=f"Ciutat seleccionada: {city}")
Ciutat_e.pack()
weather_e = tk.Label(ventana, text=f"Temperatura: {temp}ºC, el qual es {(temp * 9 / 5) + 32}ºF")
weather_e.pack()
feels_e = tk.Label(ventana, text=f"Sensació térmica: {feels_like}ºC, el qual es {(feels_like * 9 / 5) + 32}ºF")
feels_e.pack()
Humid_e = tk.Label(ventana, text=f"Humitat: {Humid}%")
Humid_e.pack()
Wind_e = tk.Label(ventana, text=f"Velocitat del vent: {Wind}m/s")
Wind_e.pack()

# Crear una etiqueta
etiqueta = tk.Label(ventana)
etiqueta.pack(padx=100, pady=100) # Añadir la etiqueta a la ventana

ventana.mainloop()
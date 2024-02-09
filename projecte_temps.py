#El codi del projecte del Jofre i l'Ivan
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
    fitxer.write("\n" + "\n" + input("Digui el seu nom:\n "))
    fitxer.write("\n" + input("Digui la seva contrasenya:\n ") + "\n")


import requests  # Importa la biblioteca requests para realizar solicitudes HTTP


#import requests
API_Key = "d206fdab52fec3ab264e1f0d49aa16ba"

#once we create the GUI we will replace the city input:
city = input("Escrigui la ciutat de la qual vol obtenir la velocitat del vent: ")
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
    print(f"El temps en aquesta ciutat és: {weather}")
#temperature (converting it to Celsius)
    temp = round(data['main']['temp'] - 273.15, 2)
    print(f"La temperatura és de: {temp}ºC, la qual es {(temp * 9 / 5) + 32 }ºF")
#Feels Like (converting it to Celsius)
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    print(f"Sensació térmica: {feels_like}ºC")
#Humidity
    Humid = data['main']['humidity']
    print(f"Humitat: {Humid}%")
#Wind Speed
    Wind = data['wind']['speed']
    print(f"La velocitat del vent és de: {Wind}")

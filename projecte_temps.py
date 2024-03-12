#El codi del projecte del Jofre i l'Ivan
import tkinter as tk
import requests 
#pip install geopy es la comanda utilitzada per descargar el geopy
from geopy.geocoders import Nominatim
API_Key = "d206fdab52fec3ab264e1f0d49aa16ba"
Base_url = "http://api.openweathermap.org/data/2.5/weather"
def registrar_usuario(nom_login):
    # Per crear un arxiu amb l'informació de l'usuari
    nombre_archivo = f"{nom_login}.txt"
    with open(f"perfils/{nombre_archivo}", "w") as archivo:
        archivo.write("Informació de l'usuari:\n")
        archivo.write(f"Nombre de usuario: {nom_login}\n")
        archivo.write(f"Ciutat: {ciutat}\n")
        
#Aquest def repeteix el codi per fer una segona o tercera búsqueda
def repetir():
    city = input("Escrigui la ciutat o poble del qual vol obtenir el temps: ")
    request_url = f"{Base_url}?appid={API_Key}&q={city}"
    #URL completa = http://api.openweathermap.org/data/2.5/weather?appid=d206fdab52fec3ab264e1f0d49aa16ba&q=spain"

    # Guardarem la resposta de la URL en get_weather
    get_weather = requests.get(request_url)



    # Iniciem la API de Nominatim per guardar el pais on es troba la ciutat
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(city)

    lat = location.latitude
    lon = location.longitude

    if get_weather.status_code == 200:
        data = get_weather.json()
    
    


#Temperatura en Cº
    temp = round(data['main']['temp'] - 273.15, 2)
#Sensació Termica en Cº
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    
#Humetat
    Humid = data['main']['humidity']

#Velocitat de vent en Metres per segon
    Wind = data['wind']['speed']

    pais = read_country(city)



    # Aqui es fa la finestra gràfica 
    ventana = tk.Tk()
    ventana.title("Projecte Python 2023-2024 | Jofre i Ivan")
    Ciutat_e = tk.Label(ventana, text=f"Ciutat seleccionada: {city}")
    Ciutat_e.pack()
    Pais = tk.Label(ventana, text=f"País en el que la ciutat es troba: {pais}")
    Pais.pack()
    lon_e = tk.Label(ventana, text=f"Co-ordenadas: {lat} , {lon}")
    lon_e.pack()
    weather_e = tk.Label(ventana, text=f"Temperatura: {temp}ºC, el qual es {(temp * 9 / 5) + 32}ºF")
    weather_e.pack()
    feels_e = tk.Label(ventana, text=f"Sensació térmica: {feels_like}ºC, el qual es {(feels_like * 9 / 5) + 32}ºF")
    feels_e.pack()
    Humid_e = tk.Label(ventana, text=f"Humitat: {Humid}%")
    Humid_e.pack()
    Wind_e = tk.Label(ventana, text=f"Velocitat del vent: {Wind}m/s")
    Wind_e.pack()

    # Aqui es crea elb botó per buscar un altre poble
    etiqueta = tk.Label(ventana)
    boto = tk.Button(ventana, text="Fer una altre búsqueda", command=repetir)
    boto.pack()

    etiqueta.pack(padx=300, pady=150) 
    ventana.mainloop()


def read_country(city):
    """
    Convert cities and returns the country
    """
    geolocator = Nominatim(user_agent="google") #El user_agent pot variar, pero google es suficient.
    location = geolocator.geocode(city, language="es") #Aqui et deixa canviar l'idioma, "es" per espanyol i "en" per anglés
    country = location.address.split(',')[-1] 
    return country



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



city = input("Escrigui la ciutat o poble del qual vol obtenir el temps: ")


from geopy.geocoders import Nominatim

def read_country(city):
    """
    Convert cities and returns the country
    """
    geolocator = Nominatim(user_agent="google") #user agent can be any user agent 
    location = geolocator.geocode(city, language="es") #specified the language as some countries are in other lanaguages
    country = location.address.split(',')[-1] #split the string based on comma and retruns the last element (country)
    return country

#Creating the full URL 
request_url = f"{Base_url}?appid={API_Key}&q={city}"
#URL completa = http://api.openweathermap.org/data/2.5/weather?appid=d206fdab52fec3ab264e1f0d49aa16ba&q=spain"

# we'll store the response code here in get_weather
get_weather = requests.get(request_url)

# Importar llibreria per les co-ordenadas
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode(city)

lat = location.latitude
lon = location.longitude
#extracting the Json file

if get_weather.status_code == 200:
    data = get_weather.json()
    #weather_unscripted = data
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
    pais = read_country(city)



# Iniciar el bucle de eventos
ventana = tk.Tk()
ventana.title("Projecte Python 2023-2024 | Jofre i Ivan")
Ciutat_e = tk.Label(ventana, text=f"Ciutat seleccionada: {city}")
Ciutat_e.pack()
Pais = tk.Label(ventana, text=f"País en el que la ciutat es troba: {pais}")
Pais.pack()
lon_e = tk.Label(ventana, text=f"Co-ordenadas: {lat} , {lon}")
lon_e.pack()
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
boto = tk.Button(ventana, text="Fer una altre búsqueda", command=repetir)
boto.pack()

etiqueta.pack(padx=300, pady=150) # Añadir la etiqueta a la ventana



ventana.mainloop()

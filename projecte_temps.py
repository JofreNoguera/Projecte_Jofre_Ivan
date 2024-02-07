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

def return_weather(city):
    url = f"https://es.wttr.in/{city}?format=j1"  # Construye la URL para solicitar información meteorológica de la ciudad especificada en español y en formato JSON
    
    response = requests.get(url)  # Realiza una solicitud GET a la URL construida
    weather_dic = response.json()  # Convierte la respuesta JSON en un diccionario de Python
    
    # Extrae la temperatura actual y la descripción del clima del diccionario de clima
    temp_c = weather_dic["current_condition"][0]['temp_C']  
    desc_temp = weather_dic["current_condition"][0]['lang_es']
    desc_temp = desc_temp[0]['value']  
    
    return temp_c, desc_temp  # Devuelve la temperatura actual y la descripción del clima

def main():
    city = input("Digui el nom d'una ciutat: ")  # Solicita al usuario que introduzca el nombre de una ciudad
    temp_c, desc_temp = return_weather(city)  # Llama a la función return_weather para obtener la temperatura actual y la descripción del clima
    print(f"La temperatura actual de {city} es {temp_c} °C. {desc_temp}.")  # Imprime la temperatura actual y la descripción del clima de la ciudad especificada en español

if __name__ == '__main__':
    main()  # Llama a la función main si el script se ejecuta directamente

#EL QUE HI HA A SOTA D'AQUESTA LINEA ES SIMPLEMENT EXPERIMENTACIÓ



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
    print(weather_unscripted)

#weather
    weather = data['weather'][0]['description']
    print(f"The current weather is: {weather}")
#temperature (converting it to Celsius)
    temp = round(data['main']['temp'] - 273.15, 2)
    print(f"The current temperature is: {temp}")
#Feels Like (converting it to Celsius)
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    print(f"Feels Like: {feels_like}")
#Humidity
    Humid = data['main']['humidity']
    print(f"Humidity: {Humid}")
#Wind Speed
    Wind = data['wind']['speed']
    print(f"Wind Speed: {Wind}")

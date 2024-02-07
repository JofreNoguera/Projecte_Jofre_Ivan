




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
    city = input("Enter a city: ")  # Solicita al usuario que introduzca el nombre de una ciudad
    temp_c, desc_temp = return_weather(city)  # Llama a la función return_weather para obtener la temperatura actual y la descripción del clima
    print(f"La temperatura actual de {city} es {temp_c} °C. {desc_temp}.")  # Imprime la temperatura actual y la descripción del clima de la ciudad especificada en español

if __name__ == '__main__':
    main()  # Llama a la función main si el script se ejecuta directamente


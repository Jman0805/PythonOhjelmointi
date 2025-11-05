import json
import requests

kunta = input("Anna paikkakunta: ")
api = "" #poistettu julkista versiota varten

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={kunta}&limit={1}&appid={api}"

try:
    vastaus = requests.get(pyyntö).json()
    vastaus = vastaus[0]

    lat = vastaus["lat"]
    lon = vastaus["lon"]
    
    pyyntö = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

    try:
        vastaus = requests.get(pyyntö).json()


        sää = vastaus["weather"][0]["description"]
        celsius = round(vastaus["main"]["temp"] - 273.15, 1)

        print(f"Säätila: {sää} Lämpötila: {celsius}°C")

    except requests.exceptions.RequestException as e:
        print ("Virhe haussa.")

except requests.exceptions.RequestException as e:
    print ("Virhe haussa.")
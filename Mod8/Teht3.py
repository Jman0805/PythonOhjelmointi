import mysql.connector
from geopy import distance

def hae_koodilla(icao1,icao2):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao1,))
        tulos1 = kursori.fetchall()
        kursori.execute(sql, (icao2,))
        tulos2 = kursori.fetchall()

        if tulos1 and tulos2:
            dist = distance.distance((tulos1), (tulos2)).km
            print(f"Lentokenttien välinen matka: {dist:.2f} km")
        else:
            print("Lentokenttiä ei löytynyt.")
        kursori.close()
    except mysql.connector.Error as err:
        print(f"Virhe kyselyssä: {err}")

try:
    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="Juho",
        password="salasana", # Piilotettu githubia varten
        autocommit=True
    )
except mysql.connector.Error as err:
    print(f"Virhe tietokantayhteydessä: {err}")
    exit(1)

icao1 = input("Anna ICAO koodi: ")
icao2 = input("Anna toinen ICAO koodi: ")
hae_koodilla(icao1, icao2)
yhteys.close()
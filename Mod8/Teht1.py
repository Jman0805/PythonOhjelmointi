import mysql.connector

def hae_koodilla(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchall()
        if tulos:
            for rivi in tulos:
                print(f"Lentokentän nimi: {rivi[0]} ja sijaintikunta: {rivi[1]}")
        else:
            print("Lentokenttää ei löytynyt.")
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

icao = input("Anna lentokentän ICAO-koodi: ")
hae_koodilla(icao)
yhteys.close()
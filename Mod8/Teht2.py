import mysql.connector

def hae_koodilla(icao):
    sql = "SELECT type FROM airport WHERE iso_country = %s"
    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchall()
        
        if tulos:
            for rivi in tulos:
                smallapnum = sum(1 for rivi in tulos if rivi[0] == "small_airport")
                medapnum = sum(1 for rivi in tulos if rivi[0] == "medium_airport")
                bigapnum = sum(1 for rivi in tulos if rivi[0] == "large_airport")
                closedapnum = sum(1 for rivi in tulos if rivi[0] == "closed")
                heliapnum = sum(1 for rivi in tulos if rivi[0] == "heliport")
                seaapnum = sum(1 for rivi in tulos if rivi[0] == "seaplane_base")
                ballapnum = sum(1 for rivi in tulos if rivi[0] == "balloonport")

            print(f"Maassa on pieniä lentokenttiä: {smallapnum}, keskikokoisia lentokenttiä: {medapnum}, isoja lentokenttiä: {bigapnum}, helikopterikenttiä: {heliapnum} suljettuja lentokenttiä: {closedapnum}, kuumailmapallokenttiä: {ballapnum} ja vesitasokenttiä: {seaapnum}")
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

icao = input("Anna maakoodi: ")
hae_koodilla(icao)
yhteys.close()
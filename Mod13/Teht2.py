from flask import Flask
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False
@app.route('/kenttä/<icao>')
def kenttä(icao):

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchall()
        if tulos:
            for rivi in tulos:
                nimi = rivi[0]
                kaupunki = rivi[1]
            vastaus = {
                "ICAO" : icao,
                "Name" : nimi,
                "Municipality" : kaupunki
            }

            return vastaus
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
        user="root",
        password="salasana", # Piilotettu githubia varten
        autocommit=True
    )
except mysql.connector.Error as err:
    print(f"Virhe tietokantayhteydessä: {err}")
    exit(1)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
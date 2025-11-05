class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} Kirjoittaja: {self.kirjoittaja} Sivumäärä: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} Päätoimittaja: {self.toimittaja}")


j1 = Lehti("Aku Ankka", "Aki Hyyppä")
j2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

j1.tulosta_tiedot()
j2.tulosta_tiedot()
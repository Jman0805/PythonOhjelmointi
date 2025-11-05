import random

class Auto:
    def __init__(self, rekisteri, maxnopeus):
        self.rekisteri = rekisteri
        self.maxnopeus = maxnopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeus):
        if self.nopeus + nopeus > self.maxnopeus:
            self.nopeus = self.maxnopeus
        elif self.nopeus + nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeus

    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.tunnit = 0

    def tunti_kuluu(self):
        self.tunnit += 1
        for auto in self.autot:
            rndNopeus = random.randrange(-10,16)
            auto.kiihdytä(rndNopeus)
            auto.kulje(1)
            if auto.matka > self.pituus:
                return True
            
        if self.tunnit % 10 == 0:
            self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for auto in self.autot:
            print (f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.maxnopeus} km/h, nopeus: {auto.nopeus}, kuljettu matka: {auto.matka}." )

    def kilpailu_ohi(self):
        loppu = False
        for auto in self.autot:
            if auto.matka > self.pituus:
                loppu = True
        return loppu

autot = []

for x in range(10):
    rndRekisteri = "ABC-" + str(x + 1)
    rndMaxnopeus = random.randrange(100,201)
    auto1 = Auto(rndRekisteri, rndMaxnopeus)
    print (f"Rekisteri: {auto1.rekisteri}, huippunopeus: {auto1.maxnopeus} km/h, nopeus: {auto1.nopeus}, kuljettu matka: {auto1.matka}." )
    autot.append(auto1)

kilpa = Kilpailu("Suuri romuralli", 8000, autot)

while True:
    kilpa.tunti_kuluu()
    if kilpa.kilpailu_ohi():
        break

kilpa.tulosta_tilanne()
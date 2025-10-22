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

class Sähköauto(Auto):
    def __init__(self, rekisteri, maxnopeus, akku):
        self.akku = akku
        super().__init__(rekisteri, maxnopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, maxnopeus, tankki):
        self.akku = tankki
        super().__init__(rekisteri, maxnopeus)


auto1 = Sähköauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

autot = [auto1, auto2]

auto1.kiihdytä(130)
auto2.kiihdytä(140)

for i in range(3):
    for auto in autot:
            rndNopeus = random.randrange(-10,16)
            auto.kiihdytä(rndNopeus)
            auto.kulje(1)

for auto in autot:
    print (f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.maxnopeus} km/h, nopeus: {auto.nopeus}, kuljettu matka: {auto.matka}." )

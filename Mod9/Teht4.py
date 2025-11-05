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

autot = []

for x in range(10):
    rndRekisteri = "ABC-" + str(x + 1)
    rndMaxnopeus = random.randrange(100,201)
    auto1 = Auto(rndRekisteri, rndMaxnopeus)
    print (f"Rekisteri: {auto1.rekisteri}, huippunopeus: {auto1.maxnopeus} km/h, nopeus: {auto1.nopeus}, kuljettu matka: {auto1.matka}." )
    autot.append(auto1)

loppu = False

while loppu == False:
    for auto in autot:
        rndNopeus = random.randrange(-10,16)
        auto.kiihdytä(rndNopeus)
        auto.kulje(1)
        if auto.matka > 10000:
            loppu = True #laskee loputkin vielä ennen loopin katkaisua

for auto in autot:
    print (f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.maxnopeus} km/h, nopeus: {auto.nopeus}, kuljettu matka: {auto.matka}." )
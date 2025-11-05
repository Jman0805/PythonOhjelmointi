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
        self.matka = self.nopeus * aika

auto1 = Auto("ABC-123", 142)
print (f"Rekisteri: {auto1.rekisteri}, huippunopeus: {auto1.maxnopeus} km/h, nopeus: {auto1.nopeus}, kuljettu matka: {auto1.matka}." )

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print (f"Nopeus: {auto1.nopeus}")

auto1.kiihdytä(-200)

print (f"Nopeus: {auto1.nopeus}")
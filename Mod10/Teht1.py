class Hissi:
    def __init__(self, alak, yläk):
        self.alak = alak
        self.yläk = yläk
        self.nyk = alak

    def siirry_kerrokseen(self, kerros):
        if self.nyk < kerros:
            for x in range(kerros - self.nyk):
                self.kerros_ylös()
        elif self.nyk > kerros:
            for x in range(self.nyk - kerros):
                self.kerros_alas()

    def kerros_ylös(self):
        self.nyk = self.nyk + 1
        print(f"Nykyinen kerros: {self.nyk}")

    def kerros_alas(self):
        self.nyk = self.nyk - 1
        print(f"Nykyinen kerros: {self.nyk}")

class Talo:
    def __init__(self, alak, yläk, hissiM):
        self.hissit = []
        self.alak = alak
        self.yläk = yläk
        for x in range(hissiM):
            hissi = Hissi(alak, yläk)
            self.hissit.append(hissi)
        print(self.hissit)
    
    def aja_hissiä(self, hissiN, kerros):
        hissi = self.hissit[hissiN - 1]
        hissi.siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Palohälytys")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alak)


talo1 = Talo(1, 6, 2)
talo1.aja_hissiä(1, 3)
talo1.palohälytys()
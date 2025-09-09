vuodenajat = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")

kuukausi = int(input("Anna kuukausi (1-12): "))

vuodenaika = vuodenajat[kuukausi - 1]
print(f"Kuukauden {kuukausi} vuoden aika on {vuodenaika}.")
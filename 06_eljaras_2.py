
def milyen_szam(eldontendo):
    if eldontendo < 0:
        print("A szám negatív")
    elif eldontendo > 0:
        print("A szám pozitív")
    elif eldontendo == 0:
        print("A szám egyenlő nullával")

    else:
        print("Váratlan hiba")


plusz_szam = True

while plusz_szam:
    eldontendo = input("Adj meg egy számot amit eldöntenél, hogy pozitív/negatív/nulla. ")
    if eldontendo == "":
        print("Nem adtál meg számot, viszlát")
        plusz_szam = False
    else:
        plusz_szam = True
        milyen_szam(int(eldontendo))

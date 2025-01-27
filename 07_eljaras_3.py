'''
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!

'''

szavak = []


for i in range(3):
    hozzaadando = input(str("Kérlek adj meg egy szót: "))
    szavak.append(hozzaadando)

def legrovidebb():
    legrovidebb_szo = min(szavak)

print("A lista elemei: ", szavak)

legrovidebb = min(szavak)


print(f"A legrövidebb szó a(z) {legrovidebb}")

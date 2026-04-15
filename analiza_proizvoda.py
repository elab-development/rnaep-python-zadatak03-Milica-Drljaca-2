import random
import math

# 1.Lista proizvoda koja sadrži najmanje 8 naziva proizvoda (string).

proizvodi = [
    "Laptop",
    "Miš",
    "Tastatura",
    "Monitor",
    "Slušalice",
    "Veb kamera",
    "USB hub",
    "SSD disk"
]

# 2. Rečnik koji svakom proizvodu dodeljuje cenu u evrima (float).

cene = {
    "Laptop":     950.99,
    "Miš":         19.99,
    "Tastatura":   49.99,
    "Monitor":    299.99,
    "Slušalice":   89.99,
    "Veb kamera":  59.99,
    "USB hub":     24.99,
    "SSD disk":   109.99,
}

# 3. Prikaz svih proizvoda i njihovih cena na standardnom izlazu 

print("=" * 40)
print("        LISTA PROIZVODA")
print("=" * 40)
for naziv in proizvodi:
    print(f"  * {naziv} - {cene[naziv]} €")
print()

# 4. Unos budžeta od strane korisnika. Ispis proizvoda koje korisnik može da priušti

try:
    budzet = float(input("Unesite Vaš budžet (EUR): "))
except ValueError:
    print("Nevažeći unos. Postavljam budžet na 0.")
    budzet = 0.0
 
print(f"\nProizvodi koje možete priuštiti sa budžetom {budzet:.2f} €:")
dostupni = [naziv for naziv in proizvodi if cene[naziv] <= budzet]
if dostupni:
    for naziv in dostupni:
        print(f"  * {naziv} - {cene[naziv]} €")
else:
    print("  Nema proizvoda u okviru vašeg budžeta.")
print()

# 5. Funkcija: najskuplji proizvod

def najskuplji_proizvod(recnik_cena):
    naziv = max(recnik_cena, key = recnik_cena.get)
    return naziv, recnik_cena[naziv]
 
ime, cena = najskuplji_proizvod(cene)
print(f"Najskuplji proizvod: {ime} ({cena} €)")
print()

# 6. Random modul – simulacija klika korisnika

kliknuti = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {kliknuti}")
print()

# 7. Math modul – prosečna cena zaokružena na 2 decimale

prosecna = math.floor(sum(cene.values()) / len(cene) * 100) / 100
print(f"Prosečna cena svih proizvoda: {prosecna} €")
print()
 

# 8. Broj prodatih komada i ukupan prihod

prodato = [12, 85, 60, 8, 35, 22, 50, 17]
 
ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodato[i]
print(f"Ukupan prihod od prodaje: {ukupan_prihod:.2f} €")
print()
 

# 9. Dodavanje novog proizvoda

novi_naziv = "Podloga za miš"
nova_cena  = 14.99
 
proizvodi.append(novi_naziv)
cene[novi_naziv] = nova_cena
prodato.append(40)  # ažuriramo i listu prodatih komada
 
print("Ažurirana lista proizvoda (nakon dodavanja novog):")
for naziv in proizvodi:
    print(f"  - {naziv}")
print()
 

# 10. Sortiranje proizvoda po ceni (od najjeftinijeg)

print("=" * 40)
print("   PROIZVODI SORTIRANI PO CENI")
print("=" * 40)
sortirani = sorted(proizvodi, key=lambda naziv: cene[naziv])
for naziv in sortirani:
    print(f" * {naziv} - {cene[naziv]} €")
print()


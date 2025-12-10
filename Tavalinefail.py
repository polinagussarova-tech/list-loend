from Moodulifail import *

#5
summa=float(input("Sisesta hoiuse summa: "))
aastad=int(input("Sisesta aastate arv: "))
lõpp_summa=bank(summa, aastad)
print(f"Lõppsumma {aastad} aasta pärast on {lõpp_summa:.2f} eurot")

#4
kuu=season(input("Sisesta kuu number (1-12): "))
print(f"Aastaaja on: {kuu}")


#3
print("Arvutame ruudu pindala ja ümbermõõtu!")
külg=float_kontroll(input("Sisesta ruudu külje pikkus: "))
ümbermõõt,pindala,diagonaal=square(külg)
print(f"Ruudu külg: {külg}")
print(f"Ruudu ümbermõõt: {ümbermõõt}")
print(f"Ruudu pindala: {pindala}")
print(f"Ruudu diagonaal: {diagonaal}")



#2
for i in range(3):
    aasta=int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} on tavaline aasta")



  #1
print("Lahendame/testimine mitu arvutehet!")
for i in range(5):

    arv1=float_kontroll(input("Sisesta esimene arv: "))
    arv2=float_kontroll(input("Sisesta teine arv: "))

    t=input("Sisesta tehe (+,-,*,/): ")
    tulemus=arithmetic(arv1,arv2,t)
    print(f"{arv1}{t}{arv2} = {tulemus}")


#6
n = int(input("Sisesta arv (0–1000): "))

if is_prime(n):
    print(f"{n} on algarv!")
else:
    print(f"{n} ei ole algarv.")

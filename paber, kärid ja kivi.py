#paber, käärid ja kivi mäng 
import random

valikud=["kivi", "paber", "käärid"]
mangijad=["Inimene", "Robot"]
random.shuffle(mangijad)
print(f"Mängijate järjekord: {mangijad}")
punktid={"Inimene": 0, "Robot": 0}
vooru_valikud=[]
vooru_tulemused=[]

while True:
    while True:
        kasutaja_valik = input("Sisesta kivi, paber või käärid: ").lower()
        if kasutaja_valik in valikud:
            break
        else:
            print("Vale valik! Palun proovi uuesti.")

    arvuti_valik=random.choice(valikud)
    print(f"Robot valis: {arvuti_valik}")

    vooru_valikud.append((kasutaja_valik, arvuti_valik))

    if kasutaja_valik==arvuti_valik:
        tulemus="Viik"
        print("Viik!")
    elif (kasutaja_valik=="kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik=="paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik=="käärid" and arvuti_valik == "paber"):
        tulemus="Inimene võitis"
        punktid["Inimene"]+=1
        print("Sa võitsid!")
    else:
        tulemus="Robot võitis"
        punktid["Robot"]+=1
        print("Robot võitis!")

    vooru_tulemused.append(tulemus)

    print("Punktid:")
    print(f"Inimene: {punktid['Inimene']}")
    print(f"Robot: {punktid['Robot']}")

    uuesti=input("Kas mängida järgmine voor? (jah/ei): ").lower()
    if uuesti!="jah":
        break

print("Mäng lõppes")
print(f"Lõplik tabel: {punktid}")


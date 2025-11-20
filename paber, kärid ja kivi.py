#paber, käärid ja kivi mäng 
import random

valikud = ["kivi", "paber", "käärid"]
mangijad = ["Inimene", "Robot"]
random.shuffle(mangijad)
print("Mängijate järjekord:", mangijad)
punktid = {"Inimene": 0, "Robot": 0}

vooru_valikud = []
vooru_tulemused = []
while True:
    while True:
        kasutaja_valik = input("Sisesta kivi, paber või käärid: ").lower()
        if kasutaja_valik in valikud:
            break
        else:
            print("Vale valik! Palun proovi uuesti.")
    arvuti_valik = random.choice(valikud)
    print(f"Robot valis: {arvuti_valik}")

    vooru_valikud.append((kasutaja_valik, arvuti_valik))
    if kasutaja_valik == arvuti_valik:
        tulemus = "Viik"
        print("Viik!")
    elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik == "paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik == "käärid" and arvuti_valik == "paber"):
        tulemus = "Inimene võitis"
        punktid["Inimene"] += 1
        print("Sa võitsid!")
    else:
        tulemus = "Robot võitis"
        punktid["Robot"] += 1
        print("Robot võitis!")

    vooru_tulemused.append(tulemus)
    print("\nPunktid:")
    print("Inimene:", punktid["Inimene"])
    print("Robot:", punktid["Robot"])
    uuesti = input("\nKas mängida järgmine voor? (jah/ei): ").lower()
    if uuesti != "jah":
        break
print("\n=== MÄNG LÕPPES ===")
print("Voorude valikud:", vooru_valikud)
print("Voorude tulemused:", vooru_tulemused)
print("Lõplik tabel:", punktid)


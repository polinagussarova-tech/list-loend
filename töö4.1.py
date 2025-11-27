#1️ Sõna või lause analüüs
#Sisesta sõna või lause.
#Loenda:
#mitu täishäälikut 
#mitu kaashäälikut 
#kui sisestati lause – loenda ka tühikud ja kirjavahemärgid
#import string

#t=[ 'a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö', 'õ']
#k=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
#m=string.punctuation + string.whitespace
#sõna_lause=input("Sisesta sõna või lause: ").lower()
#täishäälikud=0
#kaashäälikud=0
#märgid=0
#for täht in sõna_lause:
#    if täht in t:
 #       täishäälikud+=1
#    elif täht in k:
#        kaashäälikud+=1
#    elif täht in m:
#        märgid+=1
#print(f"Sõnas/lausees on {täishäälikud}täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")


#2️⃣ Loendid
#2.1 Nimed 👥
#Küsi kasutajalt viis nime.
#Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
#Kuva viimane lisatud nimi.
#Lisa võimalus nimekirjas olevaid nimesid muuta ✍️
#nimed=[]

#for i in range(5):
  #  küsimus=input("Sisesta palun 5 nime: ")
  #  nimed.append(küsimus)

#print(nimed)
#viimane_nimi=nimed[-1]
#nimed.sort()
#print(nimed)
#print(viimane_nimi)

#muuda=input("Kas sa tahad muuta nimi? ")
#if muuda=="jah":
 #   vana_nimi=input("Mis nimi muutame?")
  #  uus_nimi=input("Mis uus nimi?")
  #  find=nimed.index(vana_nimi)
 #   nimed[find]=uus_nimi
  #  print(nimed)
#else:
    #print(nimed)



#2.2 Kordustega nimed
#Antud on loend kordustega.
#Koosta programm, mis väljastab nimed ilma kordusteta.
#nimed=["Mari", "Jüri", "Kati", "Mari", "Peeter", "Jüri", "Anna"]
#ilma_kordusteta=list(set(nimed))
#print(ilma_kordusteta)

#2.3 Vanused
#Koosta vanuste loend ja leia:
#suurim
#väikseim
#kogusumma
#keskmine

#vanused=[12, 45, 23, 67, 34, 89, 10]
#suurim=max(vanused)
#väikseim=min(vanused)
#kogusumma=sum(vanused)
#keskmine=kogusumma/len(vanused)
#print(f"Suurim vanus on {suurim}")
#print(f"väikseim vanus on {väikseim}")
#print(f"kogusumma on {kogusumma}, keskmine on {keskmine:.2f}")

#3️⃣ Tärnide lintdiagramm ⭐
#Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
#******************
#*******************
#********************************
#*****************************************
#****************************************************
#************

arvud=[18, 19, 32, 41, 52, 12]
for arv in arvud:
    print("*" * arv)

# Postiindeks
#Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:
#1 – Tallinn 
#2 – Narva, Narva-Jõesuu 
#3 – Kohtla-Järve 
#4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa 
#5 – Tartu linn 
#6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa 
#7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa 
#8 – Pärnumaa 
#9 – Läänemaa, Hiiumaa, Saaremaa
#Kontrolli kasutaja sisestatud postiindeksit.
#Näita, millisesse maakonda see kuulub.
#Erireegel:
#Tallinn, Narva, Kohtla-Järve → „Mine merre!”
#Teised → „Mine metsa!”

postindeks=input("Sisesta postiindeks: ")
if len(postindeks)==5 and postindeks.isdigit():
    esinumber=postindeks[0]
    if esinumber=="1":
        print("Tallinn - Mine merre!")
    elif esinumber=="2":
        print("Narva, Narva-Jõesuu - Mine merre!")
    elif esinumber=="3":
        print("Kohtla-Järve - Mine merre!")
    elif esinumber=="4":
        print("Ida-Virumaa, Lääne-Virumaa, Jõgevamaa - Mine metsa!")
    elif esinumber=="5":
        print("Tartu linn - Mine metsa!")
    elif esinumber=="6":
        print("Tartumaa, Põlvamaa, Võrumaa, Valgamaa - Mine metsa!")
    elif esinumber=="7":
        print("Viljandimaa, Järvamaa, Harjumaa, Raplamaa - Mine metsa!")
    elif esinumber=="8":
        print("Pärnumaa - Mine metsa!")
    elif esinumber=="9":
        print("Läänemaa, Hiiumaa, Saaremaa - Mine metsa!")
    else:
        print("Vale postiindeks!")
else:
    print("Postiindeks peab olema 5-kohaline number!")
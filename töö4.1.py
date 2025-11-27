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

#3️ Tärnide lintdiagramm ⭐
#Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
#******************
#*******************
#********************************
#*****************************************
#****************************************************
#************

#arvud=[18, 19, 32, 41, 52, 12]
#for arv in arvud:
#    print("*" * arv)

#4 Postiindeks
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

#index={"Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"}
#while True:
  #  try:
  #      index=int(input("Sisesta oma postiindeks (5-kohaline arv):"))
  #      if 10000<=index<=99999:
   #         break
   #     else:
   #         print("Postiindeks peab olema 5-kohaline arv")
  #  except:
  #      print("Vigane andmetüüp")
#index_list=list(str(index))
#n1=int(index_list[0])
#print(f"Sinu postiindeks {index} kuulub piirkonda: {index_list[n1-1]}")
#if n1 in [0,1, 2, 7]:
  #  print("Mine merre!")
#else:
  #  print("Mine metsa!")


#5️ Vahetus 
#Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
#Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.

#from random import *
#loend_arvud=[]
#loend_tähed=[]
#k=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
#loend_kaashäälikud=[]
#mitu=randint(2,20)
#for i in range(mitu):
 #   elem=randint(0,100)
 #   loend_arvud.append(elem)
 #   elem=chr(randint(65,90))
 #   loend_tähed.append(elem)
 #   elem=choice(k)
 #   loend_kaashäälikud.append(elem)
#print(f"Kokku on {mitu} elemente loendis")
#while True:
   # try:
    #    paaride_arv=int(input(f"Sisesta mitu paari soovid vahetada? "))
   #     if 1<paaride_arv<=mitu//2:
    #        break
   #     else:
   #         print(f"arv peab olema vahemikus 1 kuni {mitu//2}")
  #  except:
   #     print("Vigane andmetüüp, proovi uuesti")

#6️„Arvud“
#Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.


#from random import *
#loend_arvud=[]
#mitu=randint(2,20)
#for i in range(mitu):
#    elem=randint(0,100)
#    loend_arvud.append(elem)
#print(f"alguses loend: {loend_arvud}")
#suurim=max(loend_arvud)
#kus_asub=loend_arvud.index(suurim)
#suurim_muudatud=suurim/mitu
#loend_arvud[kus_asub]=round(suurim_muudatud,2)
#print(f"Muutumise järel: {loend_arvud}")


#7️ Sorteerimine 📊
#Sorteeri nimekiri numbreid absoluutväärtuse järgi
#kasvavalt ⬆️
#või kahanevalt ⬇️

#arvud = [-10, 3, -2, 15, -20, 5]
#print(f"Algne loend {arvud}")
#arvud.sort(key=abs)
#print(f"Kasvavalt (abs)  {arvud}")

#8️⃣ Võrdse pikkusega sõned 🧱
#Muuda kõik sõned loendis sama pikkusega, täites lühemad alakriipsudega _.
#Järjekorda ei tohi muuta.
#On antud:
#['tamm', 'taevas', 'elevant'] 
#['a', 'aa', 'aaa', 'aaaa', 'aaaaa'] 
#['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#Tulemus:
#['tamm___', 'taevas_', 'elevant'] 
#['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa'] 
#['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

#def võrdsusta_sõned(loend):
   # max_pikkus = max(len(s) for s in loend)
   # return [s + "_" * (max_pikkus - len(s)) for s in loend]
#
#loend1 = ['tamm', 'taevas', 'elevant']
#loend2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#loend3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']

#print(võrdsusta_sõned(loend1))
#print(võrdsusta_sõned(loend2))
#print(võrdsusta_sõned(loend3))

#9️⃣ Nime kontroll 👤
#Programm peab :
#kontrollima, et nimi sisaldab ainult tähti ✔️
#kuvama nimega tervituse (suur algustäht) 😊
#loendama tähti, täishäälikuid ja kaashäälikuid
#kuvama nime tähed tähestiku järjekorras (ilma kordusteta) 🔤

#nimi = input("Sisesta nimi: ")

#if not nimi.isalpha():
 #   print("Nimi peab sisaldama ainult tähti!")
#else:
 #   nimi_korras = nimi.capitalize()
 #   print(f"Tere, {nimi_korras}!")

 #   täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
 #   kaashäälikud = "bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY"

 #   tähti = len(nimi)
 #   vokaalid = sum(1 for t in nimi if t in täishäälikud)
 #   konsonandid = sum(1 for t in nimi if t in kaashäälikud)

 #   print(f"Tähti kokku: {tähti}")
    #print(f"Täishäälikuid: {vokaalid}")
  #  print(f"Kaashäälikuid: {konsonandid}")

  #  unikaalsed = sorted(set(nimi.lower()))
 #   print("Tähed tähestiku järjekorras:", "".join(unikaalsed))
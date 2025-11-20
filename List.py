#list-Loend
#loome listi
#l=[]  # tühi list
#print(f"Listi alguseis: {l}")
#while True:
#    print("Tee valik: ")
 #   print("1-Lisa elemente; n2-Lisa elemente pos-le; n3-Eemalda elemente pos järgi")
 #   print("4-Eemalda element nime järgi; 5-Lisa kõik teise listi elemendid lõppu; 6-Sorteerib list")
 #   print("7-Pööra järjekorra ümber; 8-Tühjendab listi")
 #   while True:
 #       try:
 #           valik=int(input())
  #          break
 #       except:
  #          print("arvud: 1...n")
  #  print("töö listiga")

  #  if valik==1:
   #     while True:
  #          try:
   #             i=int(input("Mitu elementid soovid lisada? "))
   #             if i>0:
   #                 break
      ##          else:
    #                print("Arvud on vaja >0")
   #         except:
     #           print("Täisarvud on vaja kasutada")
    #    for element_id in range(i):
    #        element=input(f"{element_id}, element:")
    #        l.append(element)

   ## elif valik==2:
  #      while True:
  #          try:
  #              pos=int(input(f"Positsioon kuhu soovid lisada (0- {len(l)}): "))
   #             if 0<=pos<=len(l):
   #                 break
  #              else:
   #                 print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
    #        except:
    # #           print("Täisarvud on vaja kasutada")
   #     element=input("Sisesta element mida soovid lisada: ")
   #     l.insert(pos, element)

 #   elif valik==3:
#       while True:
    #        try:
    #            pos=int(input(f"Positsioon kuhu soovid lisada (0- {len(l)-1}): "))
     #           if 0<=pos<=len(l)-1:
     #               break
    #            else:
    #                print(f"Positsioon peab olema vahemikus 0 kuni {len(l)-1}")
     #       except:
    #            print("Täisarvud on vaja kasutada")
   #     eem_element=l.pop(pos)
   #     print(f"Eemaldatud element on: {eem_element}")

   # elif valik==4:
   #     element=input("Sisesta element mida soovid eemaldada: ")
  #      mitu=l.count(element)
    #    if mitu==0:
    #        print("Elementi ei leitud")
    #    else:
   #         for e in range(mitu):
   #             print(f"Eemaldane element '{element}' {l.index(element)} poositsioonilt")
   #             l.remove(element) #eemaldab esileiud elemendi
   #     print(f"Eemaldati {mitu} elementi")

  #  elif valik==5:
 #        while True:
   #         try:
  #              mitu=int(input("Mitu elementi soovid lisada? "))
  #              if mitu>0:
  #                  break
  #              else:
  #                  print("Arv peab olema>0")
   #         except:
   #             print("Täisarvud on vaja kasutada")
   #      list2=[]
   #      for i in range(mitu):
   #          element=input(f"{i}, element: ")
  #           list2.append(element)
  #       l.extend(list2)

  #  elif valik==6:
  #      try:
   #         l.sort()
 #       except:
  #          print("Sortimine on ebaõnnestus")


  #  elif valik==7:
 #       if len(l)==0:
   #         print("List on tühi, midagi ei saa ümber pöörata")
   #     else:
   #         l.reverse()
    #        print("Listi järjekord on ümber pööratud")

   # elif valik==8:
   #     l.clear()
   #     print("List on tühjendatud")


    
   # print(f"uuendatud list on {l}")

    #Loend.extend()
    #loend.sort()
    #loend.reverse()
    #loend.clear()
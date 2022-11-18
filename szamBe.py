#Számbekérő  modul
#Többféle paraméterezéssel
#2022.11.18. Lébár Olivér


def szamBe(szoveg,tort=False,minimum=False,maximum=False):
#    print(szoveg)
#    print(tort)
#    print(minimum)
    hiba=True
    while hiba:
        try:
            if tort:
                szam=float(input(szoveg))
              
            else:
                szam=int(input(szoveg))
        except:
            print("HIBÁS TE GYÁSZ!!")
        else:
            hiba= False


szamBe("Aggyyá meg számót: ",minimum=10,tort=True)

#print("dawdadaawdadwadad",end="")
#print("12222222")


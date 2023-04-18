#szín
#ajtók száma
#márka típus
#tudjobn indulni induláskor bRRrrrrrrrrrrr
#legyen rajta hangjelzés Tütü
#legyen irányjelző ami kat-kat-kat
#leszármazott amely bmw
#a bmw brümm
#az irányjelző néma
#másik class mercedes
#ennek a kürtje mondjon valami mást vÁÁÁÁÁÁÁÁÁÁÁ
#másik class Audi
#check engine ami alapból hamis de ha megnyomjuk elromlik a motor

class auto:
    szin,ajtoszam,marka,tipus=["",0,"",""]
    def __init__(self,szin,ajtoszam,tipus):
        self.szin=szin
        self.ajtoszam=ajtoszam
        self.marka=marka
        self.tipus=tipus
    def indul(self):
        print("bRÜMM BRÜM BRÜMMMM")
    def dudas(self):
        print("TÜÜÜÜÜÜ-TÜÜÜÜ")
    def iranyjel(self):
        print("Kit-Kat")

k1=auto("Fos szín",4,"Lada","Niva")

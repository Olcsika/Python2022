class radio:
    def __init__(self,ora,perc,adas,nev):
        self.ora=ora
        self.perc=perc
        self.adas=adas
        self.nev=nev
    def __str__(self):
        return "Ora: {} Perc: {} Adasdb: {} Nev: {} ".format(self.ora,self.perc,self.adas,self.nev)

f=open("cb.txt")
adatok=[]

for e in f:
    adatok.append(e.strip("\n"))
adatok.pop(0)

f.close()

print(adatok)
print("3. feldat: Bejegyzések száma: {} db".format(len(adatok)))
print("4. feladat: ")
adasindit=[]
for e in adatok:
    if e[2]=="4":
        print("Volt négy adást indító sofőr.")
        break
else:
    print("Nem volt négy adást indító sofőr.")

nevecskek=[]
for e in adatok:
    nevecskek.append(e[3])
bekeres=input("5. feladat: Kérek egy nevet: ")
if bekeres in nevecskek:
    print("használta a CB-rádiót")
        
else:
    print("Nem használta a CB-rádiót")
#def AtszamolPercre():

    
#AtszamolPercre()

print("8. feladat : Sofőrök száma: ")

print("9. feladat : Legtöbb adást indító sofőr.")

    
    
    


        


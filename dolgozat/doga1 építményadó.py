f=open("utca.txt","r")

#print(f.read())
szoveg=[]
for i in f:
    szoveg.append(i)
szoveg.pop(0)

print("2. feladat. A mintában " + str(len(szoveg)) + " szerepel.")


adoszam=input("3. feladat. Egy tulajdonos adószáma: ")

for i in szoveg:
    tor=i.split(" ")
    print(tor)
if adoszam in tor:
    print("Van benne")
else:
    print("nincs benne")
    
f.close
#print(szoveg)

nev=input("Kérek egy nevet:")

print("A " + nev + " nevet írtad be.")

print("A {belsoNev} nevet írta be." .format(belsoNev=nev))

if len(nev)<5:
    print("Jó rövid név")
elif len(nev)>=10:
    print("Very big név")

be="nem végjel"
szavak=[]
while be!="":
    be=input("írj be valamit: ")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavak)-1)
#szavak=szavak[:-1]
    szavak=[x for x in szavak if x!=""]
print(szavak)

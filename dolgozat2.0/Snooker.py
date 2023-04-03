f=open("snooker.txt")
folista=[]
for e in f:
    folista.append(e.replace("\n","").split(";"))
    
f.close()

#print(folista)
elemek=folista.pop(0)
print("3. feladat: A világranglistán {} versenyző szerepel".format(len(folista)))
osszeg=[]
for e in folista:
    osszeg.append(int(e[3]))
    
#print(osszeg)
print("4. feladat: A versenyzők átlagosan {} fontot kerestek".format(float(sum(osszeg)/100)))
kina=[]
ize=[]
hely=[]
nev=[]
orszag=[]
nyeremeny=[]
for e in folista:
    if e[2] == "Kína":
        kina.append(e)

for e in kina:
    ize.append(int(e[3]))
legjo=[]
for e in kina:
    if e[3]=="285000":
        legjo.append(e)

for e in legjo:
    hely.append(e[2])

for e in legjo:
    nev.append(e[0])

for e in legjo:
    orszag.append(e[1])

for e in legjo:
    nyeremeny.append(int(e[3]))


#print(legjo)
#print(hely)
#print(kina)
#print(ize)
#print(max(ize))
   
print("5. feladat: A legjobban kereső kínai versenyző:")
print(elemek[0],":",hely[0])
print(elemek[1],":",nev[0])
print(elemek[2],":",orszag[0])
print(elemek[3],"összege: ",nyeremeny[0]*380)


van=[]
for e in folista:
    if e[2]=="Norvégia":
        print("6. feladat: A versenyzők között van norvég versenyző. ")

angol=[]
wales=[]
kinai=[]
skocia=[]
for e in folista:
    if e[2]=="Anglia":
        angol.append(e)
for e in folista:
    if e[2]=="Kína":
        kinai.append(e)

for e in folista:
    if e[2]=="Skócia":
        skocia.append(e)

for e in folista:
    if e[2]=="Wales":
        wales.append(e)



print("7. feladat: Statisztika")
print("Kína - {} fő".format(len(kinai)))
print("Angol - {} fő".format(len(angol)))
print("Wales - {} fő".format(len(wales)))
print("Skócia - {} fő".format(len(skocia)))



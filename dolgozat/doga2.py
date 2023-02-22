f=open("tancrend.txt","r")

print("2. feladat")
tancok=[]
for i in f:
    a=i.replace("\n","").split(";")
    tancok.append(a)    
print(tancok[0])
print(tancok[-3])

print("3. feladat")

mindelem=(tancok[::3])
#print(mindelem)
a=mindelem.count(['samba'])
print(a"-en szerepeltek sambában")
print("4. feladat")
b=mindelem.count(['Vilma'])
print("Vilma {} táncban szerepelt".format(b))
a=input("Kérem egy táncos nevét: ")
fiuk=[]
lányok=[]
f.close()

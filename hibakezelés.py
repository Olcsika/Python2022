

lista=["Bence","László","Ferenc"]
#lista.append("Martin")
try:
   print(lista[3])
except:
   print("valami nem jó")
else:
   print("Sikeres le futás")
finally:
   print("Ez a vége")
   
szam=""   
while szam=="":
   try:
      szam=int(input("Kérek egy számot: "))
   except ValueError as e:
      print(e)
      print("Ez nem szám")
   except:
      print("Ismeretlen szám")

print(szam)


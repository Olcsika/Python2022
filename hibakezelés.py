

lista=["Bence","László","Ferenc"]
lista.append("Martin")
try:
   print(lista[3])
except:
   print("valami nem jó")
else:
   print("Sikeres le futás")
finally:
   print("Ez a vége")
   

try:
   szam=int(input("Kérek egy számot: "))
except:
   pass


print(szam)

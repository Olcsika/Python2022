
szo=input("Kérek egy szöveget: ")
szam=""

while True:
    try:
        szam=int(input("Kérek egy számot: "))
        break

    except:
        print("ez nem jo!")

try:
    print(szo[szam]*szam)
except:
    print("Nincs ilyen betu!")

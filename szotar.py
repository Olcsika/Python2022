import random 
#ez a fv, bekér egy szót és annak jelentését
#Visszaad:a két bekérés listában
def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ " jelentése: ")
        
    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()

    return szavak
    
print(sokBeker())

def filebaIr(lista):
    f=open("szotar.txt","a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n") 
        
    f.close()

kerdesek=[]
def beolvas():
   f=open("szotar.txt","r")
   for sor in f:

      kerdesek.append(sor.replace("\n","").split(" "))
   f.close()

   
def kerdez():
    valasztott=random.choice(kerdesek)
    #print("valsztott ",valasztott)
    rossz=[]
    for i in range(3):
        temp=random.choice(kerdesek)
        #print ("temp",temp)
        while not(temp not in rossz and temp!=valasztott):
            temp=random.choice(kerdesek)

        rossz.append(temp)
        #print("rossz", rossz)

    print("-"*45)
    print("Mit jelent: "+ valasztott[0]+ "?")

    rossz.append(valasztott)
    print(rossz)
     #válasz bekérés
    abc="abcdefghijklmnopqrstuvz"
    random.shuffle (rossz)
    i=0
    for e in rossz:
        print(abc[i]+ ": " +e [1])
        i+=1

    valasz=input("Válassz: ")
    hol=abc.index(valasz)
    print(hol)
    while hol <= 4:
        try: 
            valasz=input("Válassz újra: ")
            hol=abc.index(valasz)
    
        except:
            pass
        
beolvas()
kerdez()    
#szavak=sokBeker()
#filebaIr(szavak)








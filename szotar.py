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
    random.seed(2)
    valasztott=random.choice(kerdesek)
    print("valsztott ",valasztott)
    rossz=[]
    for i in range(3):
        temp=random.choice(kerdesek)
        print ("temp",temp)
        while temp not in rossz and temp!=valasztott:
            rossz.append(temp)
        print("rossz", rossz)

    print("-"*45)
    print("Mit jelent: "+ valasztott[0]+ "?")

    rossz.appned(valasztott)
    print(rossz)

beolvas()
kerdez()    
#szavak=sokBeker()
#filebaIr(szavak)








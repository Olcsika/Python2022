#meghívjuk a matplotlb modult
#import matplotlib.pyplot as plt

def haromszog(pontok,elozmeny, melyseg=1):
    A=pontok[0]
    B=pontok[1]
    C=pontok[2]

    if melyseg>0:
        AB=[0,0]
        AC=[0,0]
        BC=[0,0]

        AB[0]=(A[0]+B[0])/2
        AB[1]=(A[1]+B[1])/2
        AC[0]=(A[0]+C[0])/2
        AC[1]=(A[1]+C[1])/2
        BC[0]=(B[0]+C[0])/2
        BC[1]=(B[1]+C[1])/2

        uj1=haromszog([A,AB,AC],elozmeny, melyseg-1)
        uj2=haromszog([AB,B,BC],elozmeny, melyseg-1)
        uj3=haromszog([AC,BC,C],elozmeny, melyseg-1)
    else:
        elozmeny+=[[A,B,C]]

#Viszzadja a elozmeny változó a értéket
    return elozmeny

#definiálunk egy függvényt melynek neve csucsBeker zárojelben a(melyiket ) a paramétere
def csucsBeker(melyiket):
#Bekéri a háromszög csucsának kordinátáit 
    A=input("Adja meg a háromszög "  + melyiket + " csúcsának koordinátáit, vesszővel elválasztva (pl.:0, 15): ")
#Helyettesíti a felesleges spaceket
    A=A.replace(" ","").split(",")
    A[0]=int(A[0])
    A[1]=int(A[1])
#Visszadja a A változó értékét
    return A

ujra=True

#amíg az újra hibas addig ismételi
while ujra:
    ujra=False
    mely=int(input("Mekkora mélységű legyen a fraktál (1-8): "))
    lista=haromszog([csucsBeker("A"),csucsBeker("B"),csucsBeker("C")],[],mely)

    for egy in lista:
        x=[]
        y=[]
        for p in egy:
            x.append(p[0])
            y.append(p[1])
        x.append(egy[0][0])
        y.append(egy[0][1])

        #plt.plot(x,y)

    print("Ha szeretne újat, az előzőt zárja be előbb!")
    #megmutatja a függvényt
    #plt.show()
    be=input("Szeretne újat (IGEN/n)? ")
    ujra=be=="IGEN"

print("Viszlát!")
    


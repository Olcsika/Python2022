#100000 random idő.

import random
f=open("idok.txt","w")

for i in range(100000 ):
    ora=random.randint(1,23)
    perc=random.randint(0,60)
    masperc=random.randint(0,60)
    #print(ora,perc,masper)

    if perc==0 or perc==1 or perc==2 or perc==3 or perc==4 or perc==5 or perc==6 or perc==7 or perc==8 or perc==9:
        perc="0" + str(perc)

    if ora==0 or ora==1 or ora==2 or ora==3 or ora==4 or ora==5 or ora==6 or ora==7 or ora==8 or ora==9:
        ora="0" + str(ora)

    if masperc==0 or masperc==1 or masperc==2 or masperc==3 or masperc==4 or masperc==5 or masperc==6 or masperc==7 or masperc==8 or masperc==9:
        masperc="0" + str(masperc)

    ossz=str(ora) + ":" + str(perc) + ":" + str(masperc)+ "\n"
    #print(ossz)

    f.write(ossz)
f.close()    

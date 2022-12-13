import random
import math

szavak=["alma","körte","barack","banón","dinnye","szőlő"]

#random.seed(1)
print( szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

nagylista=[]
for e in szavak:
    #print("-"*20)
    kislista=[]
    kislista.append(e)
    kislista.append(random.randint(12,312))
    #print(kislista)
    nagylista.append(kislista)
print(nagylista)        


for e in nagylista:
    print(e[0].rjust(10),str(e[1]).rjust(4),"kg")

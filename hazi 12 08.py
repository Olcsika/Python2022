import random
import math




a=[]
for i in range(10):
    a.append(random.randint(1,31))

b=[]
for i in range(10):
    b.append(random.randint(1,12))

c=[]
for i in range(10):
    c.append(random.randint(1900,1999))
print("évszám="+str(c))
print()
print("hónap="+str(b))
print()
print("nap="+str(a))
print()

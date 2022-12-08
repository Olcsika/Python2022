import random
import math
l=[]
for i in range(100):
   l.append(random.randint(-9999,9999))

   
#print(l)    
we=[]
for e in l:
    if e%6==0:
      we.append(e)
    
        
print(we)


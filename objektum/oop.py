#class MyClass:
  #x = 5
  #def megnovel(self,mennyivel=1):
    #self.x+=mennyivel

class kutya:
    nev,fajta,agresszivitás,kor,szín=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitás,kor,szín):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitás=agresszivitás
        self.kor=kor
        self.szín=szín


    
    def ugat(self):
        print("Vau-vau")

    def koszon(self):
        print("Vau-vau, {} vagyok ".format(self.nev))
    def talalkozas(self,masik):
        if self.agresszivitás>5 or masik.agresszivitás>5:
            #torok harapás
            if self.agresszivitás>masik.agresszivitás:
                print("Megöllek, kutya!")
            else:
                print("Ne bánts, báttya!")
        else:

            if self.agresszivitás>masik.agresszivitás:
                print("Szevasz, kutya!")
            else:
                print("Szia, báttya!")
                

                

k1=kutya("Anyád","puli",3,9,"fekete")
k2=kutya("Apád","golden retriver",1,3,"világos barna")

k1.ugat()
k1.koszon()
k2.koszon()
k2.talalkozas(k1)
"""  
print(MyClass.x)

p1=MyClass()
print(p1.x)
p2=MyClass()
p2.x=6
print(p2.x+2)

p1.megnovel()
p1.megnovel()
print(p1.x)

"""

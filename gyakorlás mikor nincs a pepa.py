E = 0
V = 0.0
EV = input("Egész vagy Valós :")
if EV == ("E"):
    E= int(input("Kérek egy egész számot: "))
    print(E*2)
elif EV == ("V"):
    V=float(input("Kérek egy valós számot: "))
    print(V*2)

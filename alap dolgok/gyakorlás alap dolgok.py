
gyumolcsok=["alma","szőlő","körte","barac","dragonfruit","licsi"]

print("Ennyi gyümölcs van: {}".format(len(gyumolcsok)))



#print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]="barack"

print(gyumolcsok.index("barac"))

#gyumolcsok[gyumolcsok.index("barac")]+="k"

index=gyumolcsok.index("barac")
gyumolcsok[index]+="kos pite"




print(gyumolcsok[3])

print("Rövid gyümölcsök")
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        print(gyumolcsok[i])







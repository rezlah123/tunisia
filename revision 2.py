t1=int(input('la moyenne du 1 er trimestre ='))
t2=int(input("la moyenne du 2 eme trimestre ="))
t3=int(input("la moyenne du 3 eme trimestre ="))
moy_gen=(t1+t2*2+t3*2)/5
print("moyenne generale =",moy_gen)
if moy_gen>=10 :
    print("admis")
else :
    print("rufise")
#les mention
if 10<=moy_gen<12 :
    print("assez bien")
elif 12<=moy_gen<14 :
    print(" bien")
elif 14<=moy_gen<16 :
    print("a bien")
elif 16<=moy_gen<18 :
    print("tres bien")


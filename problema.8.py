a=int(input('Primul numar ete '))
b=int(input('Al doilea numar este '))
c=int(input('Al treilea numar este '))
if (a<b+c) and (b<c+a) and (c<a+b):
    if (a==b==c):
        print("Aceste numere sunt laturile unui triunghi echilateral")
    elif (a==b) or (b==c) or (c==a):
        print("Aceste numere sunt laturile unui triunghi isoscel")
    else:
        print("Aceste numere sunt laturile unui triunghi scalen")
else:
    print("Aceste numere nu sunt laturile unui triunghi")
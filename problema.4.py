from fractions import Fraction
x=int(input('Introduceti numaratorul pentru prima fractiie:'))
y=int(input('Introduceti numitorul pentru prima fractie:'))
z=int(input('Introduceti numaratorul pentru a doua fractie:'))
w=int(input('Introduceti numitorul pentru a doua fractie:'))
s=Fraction(x,y)+Fraction(z,w)
p=Fraction(x,y)*Fraction(z,w)
print(f'Suma fractiilor este {s} si produsul fractiilor este {p}')
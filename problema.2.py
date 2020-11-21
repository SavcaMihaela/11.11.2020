import math
n=int(input('Numarul:'))
s=0
for i in range (1,n+1):
    s=s+math.factorial(i)
print("Suma lor este", s)
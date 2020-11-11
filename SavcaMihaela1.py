##Se da nr n, n apartine 28, 29, 30, 31, sa se afiseze denum lunilor cu nr  de zile n
n=int(input("Intorodu nr: "))
if n<28:
    print( 'Eroare')
if n==28:
    print('Februarie')
if n ==29:
    print( 'Februarie, an bisect')
if n==30:
    print('Aprilie, Iunie, Septembrie, Octombrie, Noiembrie')
if n==31:
    print('Ianuarie, Martie, Mai, Iulie, August, Octombrie, Decembrie')
if n>31:
    print('Eroare')
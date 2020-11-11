##se dau nr naturale m si n, m<n sa se verifice daca n este o putere a lui m
m=int(input("Baza puterii"))
n=int(input("Exponent a puterii"))
if m>n:
    print(n, "Nu este putere", m )
if m==n:
    print(n, "Nu este putere", m )
if m<n:
    if m**2==n:
        print(n, "Este putere", m)
    if m**2!=n:
        print(n, "Nu este putere", m)
    
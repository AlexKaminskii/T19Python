napis = str(input("Podaj wiadomość: "))
szyfr = ""
klucz = int(input("Podaj klucz: "))
for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i])-65+klucz)%26)
print("Wiadomość: ", napis, "\nZaszyfrowana wiadomość: ", szyfr)


# odejmowanie
def nwd(a, b):
    while a!=b:
        if a > b:
            a -= b
        if a < b:
            b -= a
    return a
#modulo
def nwd(a, b):
    while b > 0:
        a, b = b, a%b
    return a
#nww
def nww(a, b):
    iloczyn = a * b
    while a != b:
        if a > b:
            a -= b
        if b > a:
            b -= a
    nwd = a
    return iloczyn // nwd
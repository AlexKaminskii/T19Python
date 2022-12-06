napis = str(input("Podaj wiadomość: "))
szyfr = ""
klucz = int(input("Podaj klucz: "))
for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i])-65+klucz)%26)
print("Wiadomość: ", napis, "\nZaszyfrowana wiadomość: ", szyfr)

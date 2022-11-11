print("Zadanie 1")
p = int(input("Podaj początek: "))
k = int(input("Podaj koniec: "))
s = int(input("Podaj długość skoku: "))

for i in range(p, k + 1, s):
    if i == k:
        trafila = " Bajtożabka trafiła w koniec w jednym ze swoich skoków"
        nietrafila = ""
    else:
        nietrafila = "Bajtożabka nie dała rady trafić w koniec w żadnym ze skoków"
        trafila = ""
print(trafila, nietrafila)

if k - p < s:
    print(" Bajtożabka przekroczyła koniec w 1 skoku")
elif k - p < s * 2:
    print(" Bajtożabka przekroczyła koniec w 2 skoku")
elif k - p < s * 3:
    print(" Bajtożabka przekroczyła koniec w 3 skoku")
elif k - p < s * 4:
    print(" Bajtożabka przekroczyła koniec w 4 skoku")
elif k - p < s * 5:
    print(" Bajtożabka przekroczyła koniec w 5 skoku")
else:
    print(" Bajtożabka nie przekroczyła końca w żadnym skoku")

if (k - p) % 5 == 0:
    print(" Tak, bajtożabka trafi w koniec w piątym skoku jeżeli skok będzie wynosił", (k - p) // 5)
else:
    print(" Bajtożabka nie trafi w koniec w piątym skoku")



print()
print("Zadanie 2")

for i in range(1000,10000):
    if i % 10 == ( (i // 10) % 10) * 2 == ( ( (i // 10) // 10) % 10) * 4 and i%1000!=0:
        print(i)




print()
print("Zadanie 3")

n = int(input("Podaj nieparzystą liczbę: "))
if n%2 == 1:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i - j == 1 or i - j == 0 or i - j == - 1 or i + j == n + 1 or i + j == n or i + j == n + 2:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()
else:
    print("Liczba jest parzysta, podaj nieparzystą")

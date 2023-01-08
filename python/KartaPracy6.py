# #################################################### zad 1
# a, b, c = map(int, input().split(" "))
# if a - b == b - c:
#     print("arytmetyczny - TAK")
# else:
#     print("arytmetyczny - NIE")
#
# if a * c == b**2:
#     print("geometryczny - TAK")
# else:
#     print("geometryczny - NIE")
#
# if a<b<c:
#     print("rosnący - TAK")
# else:
#     print("rosnący - NIE")
#
# if a>b>c:
#     print("malejący - TAK")
# else:
#     # print("malejący - NIE")

# #################################################### zad 2

# suma = 0
# for i in range(100,1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma += i
# print(suma)

# ################################################### zad 3

# suma = 0
# for i in range(10, 100):
#     if i % 7 == 0:
#         a = i
#
# for i in range(1000, 10000):
#     if i % a == 0:
#         suma += 1
# print(suma)

# ################################################## zad 4

# suma = 0
# for i in range(10,100):
#     a = i//10
#     b = i%10
#     if b >= a*2:
#         suma += 1
# print(suma)

# ################################################# zad 5

# suma = 0
# ilosc = 0
# for i in range(100,1000):
#     if i // 100 > (1 % 10) + (1 // 10) % 10:
#         suma += i
#         ilosc += 1
# print("suma:", suma, "ilość", ilosc)

# ############################################### zad 6

# n = int(input())
# suma = 0
# for i in range(10,100):
#     if i % 19 == 0:
#         suma += i
#         n-=1
#     if n == 0:
#         break
#     else:
#         continue
# print(suma)

# ############################################## zad 7

# n = int(input())
# suma = 0
# for i in range(999, 99, -1):
#     if i % 37:
#         suma += i
#         n -= 1
#     if n == 0:
#         break
#     else:
#         continue
# print(suma)

############################################### zad 8

# n = int(input())
# suma = 2
# znak = -1
# a = 2
# for i in range(n):
#     suma += (a + 3) * znak
#     a += 3
#     znak = znak * -1
# print(suma)

# ############################################ zad 9

# n = int(input())
# znak = 1
# a = 1
# wynik = 1
# for i in range(n):
#     wynik = wynik * (a*-2) * znak
#     a = (a * -2) * znak
#     znak = znak * -1
# print(wynik)

# ########################################## zad 10

# def silnia(n):
#     wynik = 1
#     while n > 0:
#         wynik = wynik * n
#         n -= 1
#     return wynik
#
# n = int(input())
# wynik = 0
# for i in range(n):
#     wynik += silnia(n)
#     n -= 1
# print(wynik)

# ######################################### zad 11

# n = int(input())
# suma = 0
# for i in range(1, n+1):
#     suma += (2*i-1)/(i**2)
# print(suma)

# ######################################### zad 12

# n = int(input())
# gora = 0
# dol = 0
# for i in range(1, n+1):
#     gora += (2*i-1)
#     dol += (i**2)
# print(f"{gora}/{dol} = {gora/dol}")

# ######################################## zad 13/14

# n = int(input())
# wynik = 0
# for i in range(1, n + 1):
#     wynik += (i*2)/((i**3)+2)
# print(wynik)

# ####################################### zad 15

# n = int(input())
# b = 3
# gora = 1
# dol = 1
# for i in range(n):
#     gora = gora * b
#     b += 1
#     dol = dol * (2*i)+1
# print(f"{gora}/{dol} = {gora/dol}")

# ##################################### zad 16

# n = int(input())
# a = 1
# b = 2
# gora = 1
# dol = 1
# for i in range(n):
#     gora = gora * a
#     a, b = b, a + b
#     dol = dol * (2**i)
# print(f"{gora}/{dol} = {gora/dol}")

# def fibonacci(n):
#     a = 1
#     b = 2
#     for i in range(n):
#         print(a, end="\t")
#         a, b = b, a + b
# print(fibonacci(10))

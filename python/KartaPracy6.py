# def nwd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a



# zad 1

# a = int(input())
# b = int(input())
# c = int(input())

# if a - b == b - c:
#     print("Arytmetyczny - TAK")
# else:
#     print("Arytemtyczny - NIE")

# if a * b == c:
#     print("Geometryczny - TAK")
# else:
#     print("Geometryczny - NIE")

# if a < b < c:
#     print("Rosnący - TAK")
# else:
#     print("Rosnący - NIE")

# if a > b > c:
#     print("Malejący - TAK")
# else:
#     print("Malejący - NIE")

# zad 2

# suma = 0
# for i in range(100, 1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma += i
# print(suma)


# zad 3

# liczba = 0
# for i in range(10,100):
#     if i % 7 == 0:
#         liczba = i
# ilosc = 0
# for j in range(1000, 10000):
#     if j % liczba == 0:
#         ilosc += 1
# print(ilosc)


# zad 4


# suma = 0
# for i in range(10,100):
#     if i % 10 <= (i // 10) * 2:
#         suma += 1
# print(suma)

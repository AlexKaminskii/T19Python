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

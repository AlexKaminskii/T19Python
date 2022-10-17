# KARTA PRACY 1



#
# zad 1

#
# a = int(input())
# b = int(input())
#
#
# print(a**2+b**2)
#

# zad 2

# a = int(input())
# b = int(input())
#
# print((a+b)**2)
#

# Zad 3

# a = int(input())
# b = int(input())
#
# print((a-b)**3)


# Zad 4

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a*b*c)


# zad 5

#
# a = int(input())
# b = int(input())
#
# print(2*(a+b)/5)


# zad 6
#
# brutto = int(input())
#
# print(brutto/1.23)
#


# zad 7

# a = int(input())
# b = int(input())
#
# print(a%b)
#







# KARTA PRACY 2








# zad 1

# a = int(input())
#
# if a%3==0:
#     print("dzieli się przez 3")
# else:
#     print("nie dzieli się przez 3")


# zad 2

# a = int(input())
#
# if a>=100 and a<=999 and a%17==0:
#     print("dzieli się przez 3 i jest trzycyfrowa")
# else:
#     print("nie")


# zad 3

# wiek = int(input())
#
# if wiek>=18:
#     print("jest pełnoletni")
# else:
#     print("nie jest pełnoletni")


# zad 4

# waga = int(input())
# limit = 20
#
# if waga>=20:
#     print("nie wjeżdzaj")
# else:
#     print("możesz wjechac")


# zad 5

# a, b, c = int(input()), int(input()), int(input())
#
# if a<c and b>c or a>c and b<c:
#     print("Tak")
# else:
#     print("nie")


# zad 6

# a, p = int(input()), int(input())
#
# if ((a**p)-a)%p==0:
#     print("TAK")
# else:
#     print("NIE")


# zad 7


# p, k, s = int(input()), int(input()), int(input())
#
# if 3*s>=k-p:
#     print("Tak")
# else:
#     print("nie")






# KARTA PRACY 3






# ANKIETA


# p = int(input())
# q = int(input())
#
# if 1.3*p>q:
#     print("tak")
# else:
#     print("nie")





# zad 1


# n = int(input("Podaj ile chcesz liczb: "))
# for i in range(n):
#     print(i**3+3, end=" ")


# zad 2

# for i in range(105,1000,15):
#     print(i, end=" ")


# zad 3


# n = int(input("podaj liczbę n:\n"))
# for i in range(1, 100):
#     if n % i == 0:
#         print(i, end=" ")



# for i in range(10,22):
#   print(i, end=" ")
#
# for i in range(15,32,2):
#   print(i, end=" ")
#
# for i in range(99,9,-1):
#   print(i, end=" ")
#
# for i in range(10,100,1):
#   print(109-i, end=" ")
#
# for i in range(100,1000,20):
#   print(i, end=" ")




# zad 4


# suma = 0
# for i in range(10, 100):
#     suma = suma + i
# print(suma)


# zad 5

# n = int(input())
# suma = n*(n+1) // 2
# for i in range(n-1):
#     x = int(input())
#     suma = suma - x
# print(suma)

#zad 6

# n =8
# a = 1
# b = 2
# print(a,b,end=" ")
# for i in range(n-2):
#     a, b = b, a + b
#     print(b, end=" ")

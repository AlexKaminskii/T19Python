# zad 1

# x = int(input())
# suma = 0
# while x > 0:
#     suma += x % 10
#     x = x // 10
# print(suma)


# zad 2



# n = int(input())
import math
def pierwsza(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

# print(pierwsza(n))



# zad 3

# n = int(input())
# suma = 0
#
# for i in range(1, n):
#     if i%n == 0:
#         suma += i
# if suma == n:
#     print("Liczba jest doskonała")
# else:
#     print("Liczba nie jest doskonała")


# zad 4
#
def nwd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


# a, b = int(input()), int(input())


# if nwd(a, b) == 1:
#     print("Liczby są względnie pierwsze")
# else:
#     print("Liczby nie są względnie pierwsze")


# zad 5


# n = int(input())
# for i in range(10,20):
#     if nwd(n, i) == 1:
#         print(i)


# zad 6

# a, b = map(int, input().split("/"))
# print(f"{a//nwd(a, b)}/{b//nwd(a, b)}")


# zad 7

# a, b = map(int, input().split("/"))
# c = a // b
# print(f"{c}  {(a%b)//nwd(a, b)}/{b//nwd(a, b)}")

# zad 8

# def suma_dz(n):
#     suma = 0
#     for i in range(1, n):
#         if n % i == 0:
#             suma += i
#     return suma
#
# for i in range(1, 10000):
#     a = suma_dz(i)
#     if i == suma_dz(a) and i != a:
#         print(i, a, "to liczby zaprzyjaźnione")



# zad 9



# for i in range(10,100):
#     if pierwsza(i):
#         for j in range(10,100):
#             if pierwsza(j):
#                 print(f"{i}*{j} = {i*j}")

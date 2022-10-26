# zad 1
import math
# for i in range(1,32):
#     print(i, end=" ")

# zad 2

# n = int(input())
# for i in range(1,n+1, 2):
#     print(i**2, end=" ")

# zad 3
#                                               sposób 1
# for i in range(1137,10000,379):
#     print(i)
#                                               sposób 2
# for i in range(1000,10000):
#     if i%379==0:
#         print(i, end=" ")
#         pass

# zad 4

# for i in range(100,1000):
#     if i%5==0 or i%6==0 or i%11==0:
#         print(i, end=" ")
#         pass

# zad 5

# suma = 0
# n = int(input("Ile liczb podasz: "))
# for i in range(n):
#     a = int(input("Podaj liczbe: "))
#     suma = suma + a
# print(suma)

# zad 6

# suma = 0
# k = int(input("Podaj liczbe: "))
# for i in range(1,k+1,2):
#     suma = suma + i
# print(suma)

# zad 7

# suma = 0
# m = int(input())
# for i in range(m):
#     suma = suma + 11 + 2*i
# print(suma)

# zad 8

# suma = 0
# w0 = int(input("Kwota wejściowa: "))
# l = int(input("Okres inwestycji: "))
# suma = w0
# for i in range(1, l*12):
#     a = suma*0.06*(1/12)
#     suma = suma + a
# print(suma)

#  zad 10

# for i in range(1, 1000):
#     if i%10 == math.sqrt(i):
#         print(i)
#         pass
#     if i%100 == math.sqrt(i):
#         print(i)

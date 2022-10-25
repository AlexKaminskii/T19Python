# zad 1

# for i in range(1,32):
#     print(i)

# zad 2

# n = int(input())
# for i in range(1,n + 1,2):
#     print(i, end=" ")

# zad 3

# for i in range(1000,10000):
#     if i%379==0:
#         print(i, end=" ")
#         pass

# zad 4

# for i in range(100,1000):
#     if i%5==0 or i%6==0 or i%11==0:
#         print(i)
#         pass

# zad 5

# suma = 0
# n = int(input())
# for i in range(n):
#     a = int(input())
#     suma = suma + a
# print(suma)

# zad 6

# suma = 0
# k = int(input())
# for i in range(2,k*2+2,2):
#     suma = suma + i
# print(suma)

# zad 7

# suma = 0
# m = int(input())
# for i in range(11, (m*2)+2, 11):
#     suma = suma + i
# print(suma, end=" ")

# zad 8

# p = int(input())
# l = int(input())
# k = 0
# suma = p
# for i in range(1, l*12):
#     x = suma*0.06*(1/12)
#     suma = (suma + x)
# print(suma)



# zad 9




#  zad 10
import math



for i in range(1, 1000):
    if i%10 == math.sqrt(i):
        print(i)
        pass
    if i%100 == math.sqrt(i):
        print(i)


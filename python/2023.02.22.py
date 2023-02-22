L = [500, 200, 100, 50, 20, 10, 5, 2, 1]
W = []
x = int(input())



for i in L:
    ilosc = x//i
    if ilosc > 0:
        x = x - ilosc * i
        for j in range(ilosc):
            W.append(i)
print(W)

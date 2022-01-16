import math
liczba_cyfr = int(input())
MAXN = int(1e6 + 1)
sito = [False] * MAXN
pytania = list(map(int, input().split()))
sito[1] = True

for i in range(2, MAXN):
    if sito[i] == False:
        for k in range(i * i, MAXN, i):
            sito[k] = True

for i in range(liczba_cyfr):
    badanaLiczba = pytania[i]
    pierwiastek = math.sqrt(int(badanaLiczba))
    if ((pierwiastek % 1 != 0) or (sito[int(pierwiastek)])):
        print("NO")
    else:
        print("YES")

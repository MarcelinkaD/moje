n = int(input())
wynik = 1


if(n == 0 or n == 1):
    print(1)
else:
    for i in range(2, n+1):
        wynik *= i
    print(wynik)
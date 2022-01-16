liczba_kartek = int(input())

for k in range(liczba_kartek):
    ciagLiczb = list(map(int,input().split()))
    ile_liczb = ciagLiczb[0]
    for i in range(2, ile_liczb + 1, 2):
        print(ciagLiczb[i], end = " ")
    for i in range(1, ile_liczb + 1, 2):
        print(ciagLiczb[i], end = " ")
    print("")


skrzynie = list(map(int,input().split()))
s0, s7 = map(int,input().split())


skrzynie[0] += s0
skrzynie[1] += s7

print(skrzynie[0], skrzynie[5], skrzynie[12])

wynik = 0

for i in skrzynie:
    wynik += i

cosik = wynik // 13

print(cosik)
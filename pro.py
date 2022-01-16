liczba_programow = int(input())

programy = list(map(int, input().split()))

liczba_plyt = int(input())

plyty = list(map(int, input().split()))

przeniesione_programy = 0

programy.sort()
plyty.sort()

licznik_programow = 0
licznik_plyt = 0

while licznik_programow < liczba_programow and licznik_plyt < liczba_plyt:
    if programy[licznik_programow] <= plyty[licznik_plyt]:
        przeniesione_programy += 1
        licznik_programow += 1
        licznik_plyt += 1 
    else:
        licznik_plyt += 1

print(przeniesione_programy)

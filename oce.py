ile_ocen = int(input())

oceny = list(map(int, input().split()))

jedynki = 0

dwojki = 0

trojki = 0

czworki = 0

piatki = 0

szostki = 0

for ocena in oceny:
    if(ocena == 1):
        jedynki += 1

    if(ocena == 2):
        dwojki += 1

    if(ocena == 3):
        trojki += 1

    if(ocena == 4):
        czworki += 1

    if(ocena == 5):
        piatki += 1

    if(ocena == 6):
        szostki += 1
        

print(str(jedynki) + " " + str(dwojki) + " " + str(trojki) + " " + str(czworki) + " " + str(piatki) + " " + str(szostki))
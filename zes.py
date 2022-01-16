ile_osób = int(input())

osoby = list(map(int, input().split()))

osoby.sort()
wynik = 0

osoby.append(2 * 10**9)
osoby.append(2 * 10**9)



i = 0

if(ile_osób < 3):
    print("0")
    quit()


while(i < ile_osób):
    if(osoby[i + 2] - osoby[i] <= 1):
        wynik += 1
        i += 3
    else:    
        i += 1

print(wynik)


ile_ludzi = int(input())

ludzie = list(map(int, input().split()))

ile_klapek = int(input())

klapki = list(map(int, input().split()))

min_wzrost = int(input())

ludzie.sort()
klapki.sort()
wynik = 0 

akklapklap = ile_klapek - 1

for i in range(ile_ludzi):
    if(ludzie[i] >= min_wzrost):
        wynik += 1
        continue
    elif(akklapklap >= 0 and ludzie[i] + klapki[akklapklap] >= min_wzrost):
        wynik += 1
        akklapklap -= 1

print(wynik)
# import math
# sekundy = int(input())
# minuty = math.ceil(sekundy / 60)
# binarnie = ""
# 
# while sekundy != 0:
#     binarnie = str(sekundy % 2) + binarnie
#     sekundy //= 2
#     
# print(minuty)
# print(binarnie)

####################################

# import math
# licznik, mianownik = map(int, input().split())
# w1 = round(licznik / mianownik, 6)
# print(w1)
# l1, m1 = licznik, mianownik
# calosci = licznik // mianownik
# l1 = licznik - (calosci * mianownik)
# 
# if calosci != 0:
#     if l1 != 0:
#         print(calosci, str(l1) + "/" + str(m1))
#     else:
#         print(calosci)
# else:
#     print(str(l1) + "/" + str(m1))
#     
# d = math.gcd(l1, m1)
# l1 //= d
# m1 //= d
# 
# if calosci != 0:
#     if l1 != 0:
#         print(calosci, str(l1) + "/" + str(m1))
#     else:
#         print(calosci)
# else:
#     print(str(l1) + "/" + str(m1))

####################################

p = str(input().strip())

if int(p[-2]) % 2 == 0:
    plec = "Kobieta"
else:
    plec = "Mężczyzna"
    
suma = int(p[0]) + (3 * int(p[1])) + (7 * int(p[2])) + (9 * int(p[3])) + int(p[4]) + (3 * int(p[5])) + (7 * int(p[6])) + (9 * int(p[7])) + int(p[8]) + (3 * int(p[9])) + int(p[10])

if suma % 10 == 0:
    czy_git = "Poprawny"
else:
    czy_git = "Błędny"
    
dzien = p[4] + p[5]
miesiac = p[2] + p[3]

if p[2] == "2" or p[2] == "3":
    rok = "20" + p[0] + p[1]
    miesiac = str(int(p[2]) - 2) + p[3]
else:
    rok = "19" + p[0] + p[1]
    
print(plec)
print(czy_git)
print(rok + "-" + miesiac + "-" + dzien)
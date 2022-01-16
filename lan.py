numer, urodzenie = map(int, input().split())
numer_str = str(numer)
numer_tablica = []

# for i in numer:
#     do_appendowania = int(i)
#     numer_tablica.append(do_appendowania)

wynik = 0
wynik = int(numer_str[8]) * 2
wynik += 5
wynik *= 50
wynik += 1764
wynik -= urodzenie

print(wynik)
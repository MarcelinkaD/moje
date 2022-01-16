napis = input()

licznik_b = 0
licznik_c = 0

for literka in napis:
    if(literka == "B"):
        licznik_b = licznik_b + 1
    else:
        licznik_c = licznik_c + 1 

wynik_b = int(licznik_b / 2)
wynik_c = int(licznik_c / 2)
print(wynik_b + wynik_c)
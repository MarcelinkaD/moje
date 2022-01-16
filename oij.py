co_teraz_szukamy = "o"

transparent = input()
wynik = 0

for literka in transparent:
    if(literka == co_teraz_szukamy and co_teraz_szukamy == "o"):
        co_teraz_szukamy = "i"
    if(literka == co_teraz_szukamy and co_teraz_szukamy == "i"):
        co_teraz_szukamy = "j"
    if(literka == co_teraz_szukamy and co_teraz_szukamy == "j"):
        co_teraz_szukamy = "o"
        wynik += 1

if(wynik == 0):
    print("NIE")
else:    
    print(wynik)
    
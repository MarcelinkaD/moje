wszystkie_dzielniki = {1, 2 ,4, 8}
dzielniki_wczytane = {4, 8}


wszystkie_dzielniki.add(10)

#roznica zbiorow
nowy_zbior = wszystkie_dzielniki.difference(dzielniki_wczytane)


#suma zbiorów
suma_zbiorow = wszystkie_dzielniki.union(dzielniki_wczytane)

print(suma_zbiorow)



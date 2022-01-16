def WyszukajBinarnie(tab, liczba, ile_dzialek):
    p = 1
    k = ile_dzialek + 1 
    while p < k:
        srodek = int((k + p) / 2)
        if(liczba < tab[srodek]):
            k = srodek
        elif(liczba > tab[srodek]):
            p = srodek + 1
        else:
            return srodek
            break

    return srodek


def main():
    n, q = map(int, input().split())

    tab = list(map(int, input().split()))

    tab.insert(0, - (1000 * 1000 * 1000 + 7))
    tab.append(1000 * 1000 * 1000 + 7)

    for i in range(q):
        dzialka = int(input())
        znalezionyIndeks = WyszukajBinarnie(tab, dzialka, n)
        lewy_sasiad = tab[znalezionyIndeks]
        prawy_sasiad = tab[znalezionyIndeks + 1]
        oleglosc_prawego_dzialkowego_sasiada = prawy_sasiad - dzialka
        oleglosc_lewego_dzialkowego_sasiada = dzialka - lewy_sasiad
        wynik = min(oleglosc_lewego_dzialkowego_sasiada,
                    oleglosc_prawego_dzialkowego_sasiada)

        print(abs(wynik))

    # petla leci po ile_zapytan


# wywolanie poczatku programu
main()

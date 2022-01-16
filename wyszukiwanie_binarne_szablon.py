def WyszukajBinarnie(tab, liczba):
    p = 0
    k = len(tab)
    while p < k:
        srodek = int((k + p) / 2)
        if(liczba < tab[srodek]):
            k = srodek
        elif(liczba > tab[srodek]):
            p = srodek + 1
        else:
            print(srodek)
            break
    
    print(-1)


def main():
    tab = list(map(int, input().split()))
    szukanaLiczba = int(input())
    tab.sort()

    WyszukajBinarnie(tab,szukanaLiczba)



#wywolanie poczatku programu
main()








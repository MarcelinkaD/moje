from sys import stdin
input = stdin.readline

def main():
    rok = str(input())
    rok = str(int(rok) + 1)
    sett = set([])
    wynik = []

    while len(wynik) == 0:
        sett = set([])
        for i in rok:
            sett.add(i)

        if len(sett) == 4:
            wynik.append(rok)
        else:
            rok = str(int(rok) + 1)

    print(wynik[0])

main()
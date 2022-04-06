from sys import stdin
input = stdin.readline

def main():
    ac = int(input())
    przesuniecie = int(input())
    zaszyfrowanie = False
    napis = str(input())
    lit = 0
    zaszyfrowany_napis = []

    if(ac == 1):
        zaszyfrowanie = True
    else:
        zaszyfrowanie = False

    if(zaszyfrowanie == True):
        for literka in range(0, len(napis)):
            czy_duża = False
            if(napis[literka].isalpha()):
                badanaLiterka = napis[literka]
                if(badanaLiterka.isupper()):
                    badanaLiterka = badanaLiterka.lower()
                    czy_duża = True
                if(ord(badanaLiterka) + przesuniecie > 122):
                    nowyKod = ord(badanaLiterka) + przesuniecie - 26
                    lite = chr(nowyKod)
                    if(czy_duża == True):
                        zaszyfrowany_napis.append(lite.upper())
                    else:
                        zaszyfrowany_napis.append(lite)

                else:
                    nowyKod = ord(badanaLiterka) + przesuniecie
                    lite = chr(nowyKod)
                    if(czy_duża == True):
                        zaszyfrowany_napis.append(lite.upper())
                    else:
                        zaszyfrowany_napis.append(lite)
            else:
                zaszyfrowany_napis.append(napis[literka]) 

    if(zaszyfrowanie == False):
        for literka in range(0, len(napis)):
            czy_duża = False
            if(napis[literka].isalpha()):
                badanaLiterka = napis[literka]
                if(badanaLiterka.isupper()):
                    badanaLiterka = badanaLiterka.lower()
                    czy_duża = True
                if(ord(badanaLiterka) - przesuniecie < 97):
                    nowyKod = ord(badanaLiterka) - przesuniecie + 26
                    lite = chr(nowyKod)
                    if(czy_duża == True):
                        zaszyfrowany_napis.append(lite.upper())
                    else:
                        zaszyfrowany_napis.append(lite)

                else:
                    nowyKod = ord(badanaLiterka) - przesuniecie
                    lite = chr(nowyKod)
                    if(czy_duża == True):
                        zaszyfrowany_napis.append(lite.upper())
                    else:
                        zaszyfrowany_napis.append(lite)
            else:
                zaszyfrowany_napis.append(napis[literka]) 

    for i in zaszyfrowany_napis:
        print(i, end = "")
        
main()


def main():
    mewy = str(input())
    biale = []
    szare = []
    akt_ciag = mewy[0]
    pierwsza_literka = mewy[0]
    akt_liteka = akt_ciag[0]
    licznik = 0

    for i in range(1, len(mewy)):
        if(mewy[i] == akt_ciag[0]):
            akt_ciag += mewy[i]
        else:
            if(akt_liteka == "b"):
                biale.append(akt_ciag)
                akt_liteka = "s"
            else:
                szare.append(akt_ciag)
                akt_liteka = "b"
            
            akt_ciag = mewy[i]

    if(akt_liteka == "b"):
        biale.append(akt_ciag)
    else:
        szare.append(akt_ciag)

    biale.sort(key = len, reverse = True)
    szare.sort(key = len, reverse = True)

    if(pierwsza_literka == "s"):
        while licznik < len(szare) and licznik < len(biale):
            print(szare[licznik], end = "")
            print(biale[licznik], end = "")
            licznik += 1

        if(len(szare) < len(biale)):
            print(biale[licznik])
        elif(len(szare) > len(biale)):
            print(szare[licznik])

    else:
        while licznik < len(szare) and licznik < len(biale):
            print(biale[licznik], end = "")
            print(szare[licznik], end = "")
            licznik += 1

        if(len(szare) > len(biale)):
            print(szare[licznik])
        elif(len(szare) < len(biale)):
            print(biale[licznik])

main()
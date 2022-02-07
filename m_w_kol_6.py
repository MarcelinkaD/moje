from dataclasses import dataclass
import math

@dataclass
class ciag:    
    dlugosc: int
    literka: str
    koniec_input: int

def main():
    mewy = str(input())
    akt_ciag = 1
    akt_literka = mewy[0]
    poprzednia_literka = mewy[0]
    tab = []
    roznica = 0
    poprzednia_roznica = 0
    dlugosc_w = 0
    dlugosc_k = 0
    
    for i in range(1, len(mewy)):
        if(mewy[i] == poprzednia_literka):
            akt_ciag += 1
            poprzednia_literka = mewy[i]
        else:
            if(akt_literka == "b"):
                tab.append(ciag(akt_ciag, akt_literka, i))
                akt_literka = "s"
            else:
                tab.append(ciag(akt_ciag, akt_literka, i))
                akt_literka = "b"
            
            akt_ciag = 1
            poprzednia_literka = mewy[i]
            
    if(akt_literka == "b"):
        tab.append(ciag(akt_ciag, akt_literka, i))
    else:
        tab.append(ciag(akt_ciag, akt_literka, i))
            
    for i in range(len(tab) - 1):
        roznica = abs(tab[i].dlugosc - tab[i + 1].dlugosc)
        if(i > 0):
            poprzednia_roznica = abs(dlugosc_w - dlugosc_k)
        
        if(roznica > poprzednia_roznica):

            if(tab[i].dlugosc + tab[i + 1].dlugosc > dlugosc_w + dlugosc_k or roznica > poprzednia_roznica):
                if(tab[i].dlugosc > tab[i + 1].dlugosc):
                    dlugosc_w = tab[i].dlugosc
                    dlugosc_k = tab[i + 1].dlugosc
                else:
                    dlugosc_k = tab[i].dlugosc
                    dlugosc_w = tab[i + 1].dlugosc

        elif(roznica == poprzednia_roznica):
            if(tab[i].dlugosc + tab[i + 1].dlugosc > dlugosc_w + dlugosc_k):
                if(tab[i].dlugosc > tab[i + 1].dlugosc):
                    dlugosc_w = tab[i].dlugosc
                    dlugosc_k = tab[i + 1].dlugosc
                else:
                    dlugosc_k = tab[i].dlugosc
                    dlugosc_w = tab[i + 1].dlugosc

            
            
    print(str(dlugosc_w) + " " + str(dlugosc_k))

main()














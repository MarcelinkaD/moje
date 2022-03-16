from sys import stdin
input = stdin.readline

def main():
    liczba_czesci = int(input())
    smaki_lizaka = list(map(int, input().split()))
    ilosc_smakow = {}
    ilosc_smakow[0] = []
    ilosc_smakow[1] = []
    ilosc_smakow[2] = []
    ilosc_smakow[3] = []
    smaki_dict = {}
    ogon = 0
    glowa = -1
    wynik = liczba_czesci  + 1
    akt_wynik = 0
    
    while (ogon < liczba_czesci - 1):
        while (glowa < liczba_czesci - 1) and (akt_wynik == 0):
            glowa += 1
            
            if smaki_lizaka[glowa] in smaki_dict:
                smaki_dict[smaki_lizaka[glowa]] += 1
            else:
                smaki_dict[smaki_lizaka[glowa]] = 1
                
            
            
            ilosc_smakow[smaki_dict[smaki_lizaka[glowa]]].append(smaki_lizaka[glowa])
            
            if smaki_lizaka[glowa] in ilosc_smakow[smaki_dict[smaki_lizaka[glowa]]-1]:
                ilosc_smakow[smaki_dict[smaki_lizaka[glowa]]-1].remove(smaki_lizaka[glowa])

                
            akt_wynik = len(ilosc_smakow[3])
            
            if(akt_wynik > 0):
                wynik = min(glowa - ogon + 1, wynik)


        smaki_dict[smaki_lizaka[ogon]] -= 1
        
        if smaki_lizaka[ogon] in ilosc_smakow[smaki_dict[smaki_lizaka[ogon]] + 1]:
            ilosc_smakow[smaki_dict[smaki_lizaka[ogon]] + 1].remove(smaki_lizaka[ogon])
            ilosc_smakow[smaki_dict[smaki_lizaka[ogon]]].append(smaki_lizaka[ogon])
        
        ogon += 1
        
        
              
        akt_wynik = len(ilosc_smakow[3])
    
        if(akt_wynik > 0):
            wynik = min(glowa - ogon + 1, wynik)
    
    if wynik == liczba_czesci + 1:
        print("NIE")
    else:
        print(wynik)
    
main()
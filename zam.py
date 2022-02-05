def main():
    ilosc_komnat, ilosc_zapytan = map(int, input().split())
    komnaty = list(map(int, input().split()))
    
    komnaty.reverse()
    
    pref_komnaty = [0] * (ilosc_komnat)
    for indeks in range(0, ilosc_komnat):        
        pref_komnaty[indeks] = int(komnaty[indeks]) + pref_komnaty[indeks - 1]
    
    pref_komnaty.reverse()
    
    for i in range(ilosc_zapytan):
        odl_pot, odl_bajtka = map(int, input().split())
        
        odl_pot_od_laki = pref_komnaty[odl_pot - 1]
        odl_baj_od_laki = pref_komnaty[odl_bajtka - 1]
        czas_pot = odl_pot_od_laki / 20
        czas_baj = odl_baj_od_laki / 10
        
        if(czas_baj > czas_pot):
            print("NIE")
        else:
            print("TAK")
    
main()
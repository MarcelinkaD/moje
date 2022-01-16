liczba_tarasow, kredyty = map(int, input().split())
tarasy = [0] * liczba_tarasow


for i in range(liczba_tarasow):
     tarasy[i] = int(input())

ogon = 0
glowa = 0

aktKred = kredyty
najleprzynajBardziejDlugiGasienicowatyWynik = 0

while (ogon < liczba_tarasow - 1):
    while (glowa < liczba_tarasow - 1) and (aktKred >= 0):
        glowa += 1
        roznicaMiedzyTarasem = tarasy[glowa] - tarasy[glowa - 1]
        if roznicaMiedzyTarasem <= 0:
            roznicaMiedzyTarasem = 0
        aktKred -= roznicaMiedzyTarasem
        
        if(aktKred >= 0):
            najleprzynajBardziejDlugiGasienicowatyWynik = max(glowa - ogon, najleprzynajBardziejDlugiGasienicowatyWynik)



    roznicaDlaOgonu  = tarasy[ogon + 1] - tarasy[ogon]
    if roznicaDlaOgonu > 0:
        aktKred += roznicaDlaOgonu
    ogon += 1


tarasy.reverse()


ogon = 0
glowa = 0
aktKred = kredyty

while (ogon < liczba_tarasow - 1):
    while (glowa < liczba_tarasow - 1) and (aktKred >= 0):
        glowa += 1
        roznicaMiedzyTarasem = tarasy[glowa] - tarasy[glowa - 1]
        if roznicaMiedzyTarasem <= 0:
            roznicaMiedzyTarasem = 0
        aktKred -= roznicaMiedzyTarasem
        
        if(aktKred >= 0):
            najleprzynajBardziejDlugiGasienicowatyWynik = max(glowa - ogon, najleprzynajBardziejDlugiGasienicowatyWynik)



    roznicaDlaOgonu  = tarasy[ogon + 1] - tarasy[ogon]
    if roznicaDlaOgonu > 0:
        aktKred += roznicaDlaOgonu
    ogon += 1

print(int(najleprzynajBardziejDlugiGasienicowatyWynik))

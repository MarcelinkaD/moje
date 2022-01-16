liczbak, liczbam = map(int, input().split())

ks = list(map(int, input().split()))

ogon = 0
glowa = 0
najleprzynajBardziejDlugiGasienicowatyWynik = 0
aktualnyBibliotecznyCzasczytaniaAktualny = 0



while (ogon < liczbak):
    while (glowa < liczbak) and (aktualnyBibliotecznyCzasczytaniaAktualny <= liczbam):
        aktualnyBibliotecznyCzasczytaniaAktualny += ks[glowa]
        glowa += 1
        if(aktualnyBibliotecznyCzasczytaniaAktualny <= liczbam):
            najleprzynajBardziejDlugiGasienicowatyWynik = max(glowa - ogon, najleprzynajBardziejDlugiGasienicowatyWynik)
    aktualnyBibliotecznyCzasczytaniaAktualny -= ks[ogon]
    ogon += 1

print(int(najleprzynajBardziejDlugiGasienicowatyWynik))
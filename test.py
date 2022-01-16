liczbaGlow = 84
liczbaNog= 252

ilePelnychDwojek = 0

while (liczbaNog - (2*liczbaGlow) >=0):
    if(liczbaNog - (2*liczbaGlow) >=0):
        liczbaNog-=(2*liczbaGlow)
        ilePelnychDwojek+=1

if(ilePelnychDwojek == 1):
    liczbaGlowZDodatkowymiNogamiWOstatnimPrzebieguCzyliKrowy = liczbaNog / 2
else:
    liczbaGlowZDodatkowymiNogamiWOstatnimPrzebieguCzyliKrowy = liczbaGlow
kury = liczbaGlow - liczbaGlowZDodatkowymiNogamiWOstatnimPrzebieguCzyliKrowy
print(str(int(kury))+" "+str(int(liczbaGlowZDodatkowymiNogamiWOstatnimPrzebieguCzyliKrowy)))

godziny = 23
minuty = 59
sekundy = 59

sekundy = sekundy + 1 

if (sekundy == 60):
    sekundy = 0
    minuty = minuty + 1

if (minuty == 60):
    minuty = 0
    godziny = godziny + 1

if (godziny == 24):
    godziny = 0

def zero_napoczatku(liczba):
    if (liczba < 10):
     return str(0) + str(liczba)
    else:
        return str(liczba)
print(zero_napoczatku(godziny) + ":" + zero_napoczatku(minuty) + ":" + zero_napoczatku(sekundy))

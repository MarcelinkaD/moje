ilośćpętli = int(input())

listawyników = [0] * ilośćpętli

#start - petla liczaca wyniki
for i in range(ilośćpętli):
    linia = input()
    wynik = 0
    asy = 0 # tutaj powinna byc zmienna
    for k in linia:
        if(k.isdigit()):
           wynik += int(k)     
        elif(k == "T" or k == "Q" or k == "J" or k == "K"):
            wynik += 10
        elif(k == "A"):
            asy += 1

    najlepszyWynikZAsami = wynik
    

    #asy - start
    for o in range(0, asy + 1):
        punktyZaAsy = (asy - o) * 1 + o * 11
        if(punktyZaAsy + wynik <= 21) and (punktyZaAsy + wynik > najlepszyWynikZAsami):
            najlepszyWynikZAsami = punktyZaAsy + wynik
        else:
            if(o == 0):
                najlepszyWynikZAsami = punktyZaAsy + wynik
            break
    #asy - koniec        


    if(najlepszyWynikZAsami > 21):
        listawyników[i] = 0
    else:
        listawyników[i] = najlepszyWynikZAsami
#koniec - petla liczaca wyniki

#szukamy najlepszego wyniku
najlepszyWynik = max(listawyników)


#wypisujemy najlepszy wynik
if(najlepszyWynik == 0):
    print("0")
    quit()

najlepsi = 0

for i in listawyników:
    if(najlepszyWynik == i):
        najlepsi += 1

print(najlepsi)


#kto jest najlepszy
for i in range(len(listawyników)):
    if(listawyników[i] == najlepszyWynik):
        print(str(i + 1) + " ", end = '')
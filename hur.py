ile_razy = int(input())

for liczba in range(1, ile_razy + 1):
    if(liczba % 11 == 0 and liczba % 7 == 0):
        print("Wiwat!")
        continue
    elif(liczba % 7 == 0):
        print("Hurra!")
        continue
    elif(liczba % 11 == 0):
        print("Super!")
        continue
    else:
        print(liczba)
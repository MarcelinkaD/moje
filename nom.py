def main():
    suma = int(input())
    ile_zlozylismy = 0
    trzy = 0
    dwa = 0
    
    if(suma ==  1):
        print("NO MONEY")
    elif(suma == 4):
        print(str(suma // 2) + " 0")
    elif(suma % 2 == 0 and suma % 3 == 0):
        print("0 " + str(suma // 3))
    elif(suma % 3 == 0):
        print("0 " + str(suma // 3))
    else:
        if(suma % 3 == 1):
            trzy += suma // 3 - 1
            dwa += 2
        else:
            trzy += suma // 3
            dwa += 1
    
        print(str(dwa) + " " + str(trzy))
    
main()
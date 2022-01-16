literka, liczba = map(str, input().split())

if(literka == "a" or literka == "h") and (liczba == "1" or liczba == "8"):
    print("3")

elif(literka == "a" or literka == "h") and (liczba != "1" or liczba != "8"):
    print("5")

elif(literka != "a" or literka != "h") and (liczba == "1" or liczba == "8"):
    print("5")
    
elif(literka != "a" or literka != "h") and (liczba != "1" or liczba != "8"):
    print("8")
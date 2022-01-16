n = "G z y P r z y g o t u j c i e S i e D o A t a k u"
tab = n.split()


liczbaLower = 0
liczbaUppper = 0
liczbaCos = 0

for i in tab:
    if(i.islower()):
        liczbaLower += 1
    elif(i.isupper()):
        liczbaUppper += 1
    else:
        liczbaCos += 1

print("Liczba malych liter wynosi " + str(liczbaLower))
print("Liczba dużych liter wynosi " + str(liczbaUppper))
print("Liczba pozostalych znakow wynosi " + str(liczbaCos))
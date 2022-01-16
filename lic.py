x, y, z = map(int, input().split())
wynik = 0

lista = [x, y, z]

lista.sort()

if(lista[0] == 0 and lista[1] == 0):
    pomoc = lista[0]
    lista[0] = lista[2]
    lista[2] = pomoc
elif(lista[0] == 0 and lista[1] != 0):
    pomoc = lista[0]
    lista[0] = lista[1]
    lista[1] = pomoc

for i in lista:
    print(i, end = "")
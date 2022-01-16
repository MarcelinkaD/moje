ile_prezentow = int(input())
ile_petli = 0

if(ile_prezentow % 2 == 0):
    print(int(ile_prezentow / 2))
    ile_petli = int(ile_prezentow / 2)
else:
    print(ile_prezentow // 2 + 1)
    ile_petli = int((ile_prezentow / 2) + 1)


for i in range(1, ile_petli):
    print("2 " + str(i) + " " + str(ile_prezentow - i))

print("1 " +  str(ile_prezentow))
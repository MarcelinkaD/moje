ile_zapytan = int(input())
uwolnione_zwierzaki = 0

def ObliczNWD(l1, l2):
    reszta = 0
    while l2 != 0:
        reszta = l1 % l2
        l1 = l2
        l2 = reszta
    return l1

for i in range(ile_zapytan):
    k, s = map(int, input().split())
    NWD = ObliczNWD(k, s)
    uwolnione_zwierzaki = int(k / NWD)
    print(uwolnione_zwierzaki)
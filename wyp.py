p, k = map(int, input().split())
aktualna_epicka_gorska_wysokosc = int(p)
minuty = 0



while aktualna_epicka_gorska_wysokosc != k and aktualna_epicka_gorska_wysokosc > k:
    if(aktualna_epicka_gorska_wysokosc // 2 < k and aktualna_epicka_gorska_wysokosc % 2 == 1):
        minuty += aktualna_epicka_gorska_wysokosc - k
        aktualna_epicka_gorska_wysokosc -= k
    elif(aktualna_epicka_gorska_wysokosc % 2 == 0 and aktualna_epicka_gorska_wysokosc // 2 >= k):
        aktualna_epicka_gorska_wysokosc = aktualna_epicka_gorska_wysokosc // 2
        minuty += 1
    else:
        aktualna_epicka_gorska_wysokosc -= 1
        minuty += 1

print(minuty)

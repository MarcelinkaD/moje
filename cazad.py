# https://szkopul.edu.pl/c/oki-wakacje-2023/p/ca/

from sys import stdin
input = stdin.readline

def main():
    zycie = int(input())
    y = int(input())
    moc_laseru, zwiekrzenie = map(int, input().split())
    eliksir = 0
    w = ""
    czy_zwie = False
    moc_miecza = y
    
    if zycie > moc_miecza:
        w += "B"
        zycie //= 2
    
    while zycie > 0:
        if czy_zwie:
            moc_miecza *= zwiekrzenie
            czy_zwie = False
        else:
            moc_miecza = y
        
        if moc_miecza > moc_laseru:
            w += "M"
            eliksir += 1
            zycie -= moc_miecza
        else:
            if eliksir >= 2:
                w += "L"
                zycie -= moc_laseru
                czy_zwie = True
                eliksir -= 2
            else:
                w += "M"
                eliksir += 1
                zycie -= moc_miecza
            
    print(w)
    
main()
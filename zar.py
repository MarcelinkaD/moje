from sys import stdin
input = stdin.readline

def main():
    liczba_zarowek, ilosc_klikniec = map(int, input().split())
    klikanie = list(map(int, input().split()))
    czy_wlaczona = [False] * liczba_zarowek
    wynik = 0
    
    for klik in klikanie:
        if czy_wlaczona[klik - 1] == False:
            czy_wlaczona[klik - 1] = True
            wynik += 1
        else:
            czy_wlaczona[klik - 1] = False
            wynik -= 1
            
    print(wynik)
    
main()
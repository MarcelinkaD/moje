def main():
    liczba_mew, ilosc_zapytan = map(int, input().split())
    mewy = list(map(int, input().split()))
    zapytania = list(map(int, input().split()))
    
    mewy.sort()
    
    for zapytanie in range(ilosc_zapytan):
        print(mewy[zapytania[zapytanie] - 1], end = " ")
main()
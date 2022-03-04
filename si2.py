from sys import stdin
input = stdin.readline

def main():
    liczba_ha = int(input())
    wynik = 0
    
    if liczba_ha == 1:
        print(169)
    else:
        wynik = (72 + 97 + 32) * liczba_ha
        
        print(wynik - 32)
    
main()
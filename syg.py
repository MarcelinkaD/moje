from sys import stdin
input = stdin.readline

def main():
    liczba_domow, odl = map(int, input().split())
    kanaly = list(map(int, input().split()))
    wystapienia = {}
    wynik = 0
    do_us = 0
    
    for i in range(liczba_domow):
        do_us = i - odl - 1
        if do_us >= 0:
            wystapienia[kanaly[do_us]] -= 1
            
        if kanaly[i] not in wystapienia:
            wystapienia[kanaly[i]] = 0
            
        wynik += wystapienia[kanaly[i]]            
        
        wystapienia[kanaly[i]] += 1
            

                    
    print(wynik)
        
main()
from sys import stdin
input = stdin.readline

def main():
    liczba_drzew, liczba_dni = map(int, input().split())
    drzewa = list(map(int, input().split()))
    sumy = [0] * liczba_drzew
    
    for i in range(liczba_dni):
        drzewo, wysokosc = map(int, input().split())
        drzewa[drzewo - 1] += wysokosc
        
        max_value = max(drzewa)
        wy = [index for index, value in enumerate(drzewa) if value == max_value]
        
        for k in wy:
            sumy[k] += i + 1
    
    max_value = max(sumy)
    nik = [index for index, value in enumerate(sumy) if value == max_value]
    h = min(nik)
    
    print(h + 1)
    
    
main()

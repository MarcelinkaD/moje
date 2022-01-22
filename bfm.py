def main():
    liczba_ludzi = int(input())
    
    for i in range(liczba_ludzi):
        weszlo, wyszlo = map(int, input().split())
        
        if(weszlo - wyszlo < 0):
            print((weszlo - wyszlo) * -1)
        else:
            print("SPOKO OKO")
    
main()
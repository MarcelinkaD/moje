from sys import stdin
import time
input = stdin.readline

def potegowanie(ile, do_czego):
    wynik = 1
    pot = ile
    while do_czego > 0:
        if do_czego % 2 == 1:
            wynik = wynik * pot
        pot = pot * pot
        pot %= 1000000007
        do_czego = do_czego // 2
        
    return wynik % 1000000007


def main():
    
    N = 1000000
    
    start_time = time.time()
    for i in range(N):
        pow(2,300,1000000007)
    end_time = time.time()
    avg_time = (end_time - start_time) / N
    
    print("wbudowane  milliseconds  = "+ str(avg_time * 1000))
    
    start_time = time.time()
    for i in range(N):
        potegowanie(2,300)
    end_time = time.time()
    avg_time = (end_time - start_time) / N
    
    print("wlasne  milliseconds  = "+ str(avg_time * 1000))    
    
    
    
    

main()
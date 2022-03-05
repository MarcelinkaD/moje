from sys import stdin
import math
input = stdin.readline

def main():
    n = int(input())
    wynik = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            drugi = n/i
            wynik += i
            
            if drugi != i:
                wynik += drugi
                
        
    print(int(wynik))
        
        
main()
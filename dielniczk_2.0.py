from sys import stdin
import math
input = stdin.readline

def main():
    zapytania = int(input())
    
    for i in range(zapytania):
        n = int(input())
        wynik = 0
        
        for i in range(1, int(math.sqrt(n)) + 1):
            if(n % i == 0):
                drugi = n/i
                wynik += 1
                
                if drugi != i:
                    wynik += 1
                    
        print(wynik)
    
main()
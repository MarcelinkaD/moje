from sys import stdin
import sys
sys.stdin = open("cowjog.in", "r")
sys.stdout = open("cowjog.out", "w")

def main():
    liczba_krow = int(input())
    krowy = []
    g = 0
    
    for i in range(liczba_krow):
        index, pr = map(int, input().split())
        krowy.append(pr)
    
    min = krowy[liczba_krow - 1]
    od = len(krowy) - 1
        
    for i in range(od, -1, -1):
        if krowy[i] <= min:
            g += 1
            min = krowy[i]
            
    print(g)    

main()
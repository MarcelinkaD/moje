from sys import stdin
import math
input = stdin.readline

def main():
    ile_pieter = int(input())
    pietra = [[]] * ile_pieter
    
    for i in range(ile_pieter):
        pietra[i] = []
        pietra[i].append(1)
        
        for k in range(1, math.ceil((i + 1) / 2)):
            pietra[i].append(pietra[i - 1][k - 1] + pietra[i - 1][k])
            
        for n in range(math.ceil(i / 2)- 1, -1, -1):
            pietra[i].append(pietra[i][n])
                
                
    print(pietra)
    
main()
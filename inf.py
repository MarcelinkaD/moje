from sys import stdin
from fractions import Fraction
import math
input = stdin.readline


def main():
    liczba_oszukanch_metrow = int(input())
    
    
    liczba_prawdziwych_kilometrow = Fraction(liczba_oszukanch_metrow , 1024)
    
    wynik = math.ceil(liczba_prawdziwych_kilometrow * 1000)
    print(wynik)
    
main()
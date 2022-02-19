import sys
from sys import stdin
input = stdin.readline

def main():
    znaki = 0
    linie = 0
    for linia in sys.stdin:
        czy_znak = False
        #policzyc znaki w dodatkowej petli iterujac sie po "napisie" line,
        #liczyc jesli znak jest wiekszy niż wykrzynik i mniejszy niz tylda
        for i in linia:
            if i >= "!" and i <= "~":
                znaki += 1
                czy_znak = True
        
        if czy_znak == True:
            linie += 1 # nie zawsze podbijac linie, czyli podbijac jak sa jakiekolwiek znaki
            
    print(str(linie) + " " +str(znaki))
        
    


main()
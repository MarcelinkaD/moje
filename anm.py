from sys import stdin
input = stdin.readline

def main():
    maslo_maslane = int(input())
    liczby = str(input())
    wynik = 0
    
    for i in range(0, maslo_maslane * 2, 2):
        if(liczby[i].isdigit()):
            wynik += int(liczby[i])
            
    print(wynik)
    
main()
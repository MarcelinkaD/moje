from sys import stdin
input = stdin.readline

def binary(x):
    w = ""
    
    if(x == 0):
        return "0"
    
    while x > 0:
        w = str(x % 2) + w
        x = x // 2
        
    return w
    
def main():
    liczba_10 = int(input())    
    wynik_str = binary(liczba_10)
    wynik_d = 0


    for i in wynik_str:
        wynik_d += int(i)
    
    print(str(wynik_str) + " " + str(binary(wynik_d)))
        
main()
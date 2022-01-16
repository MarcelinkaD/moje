import math

def main():               
                
    n = int(input())
    dzielnik = 2
    while(n != 1 and dzielnik <= 5): 
        if(n % dzielnik == 0):
            n //= dzielnik
        else:
            dzielnik += 1

    if(dzielnik <= 5):
        print("Bambus happy")
    else:
        print("Bambus smutny")
    
main()
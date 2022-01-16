def main():
    n = int(input())
    rozklad = []
    dzielnik = 2
    while(n != 1):
        if(n % dzielnik == 0):
            rozklad.append(dzielnik)
            n //= dzielnik
        else:
            dzielnik += 1
            
    print(rozklad)
    
main()
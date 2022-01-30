def main():
    iosc_liczb = int(input())
    liczby = list(map(int, input().split()))
    najm = 123432
    najw = -100
    
    
    najm = min(liczby)
    najw = max(liczby)
            
    print(najw - najm)
    
    
main()
def main():
    n = int(input())
    
    for i in range(n):
        pipi = int(input())
        
        if(pipi % 2 == 0):
            print("parzysta")
        else:
            print("nieparzysta")

main()
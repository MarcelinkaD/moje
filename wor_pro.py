import sys
sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")

def main():
    liczba_slow, limit = map(int, input().split())
    napis = list(map(str, input().split()))
    index = 0
    suma = 0
    
    while(index < liczba_slow):
        dany_wyraz = napis[index]
        if(len(dany_wyraz) + suma <= limit):            
            
            if(suma==0):
                print(dany_wyraz, end = "")
            else:
                print(" " + dany_wyraz, end = "")
            
            
            index += 1
            suma += len(dany_wyraz)    
        else:
            suma = 0
            print("")
            
                
main()

sys.stdin.close()
sys.stdout.close()
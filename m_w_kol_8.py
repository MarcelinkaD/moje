from sys import stdin
input = stdin.readline

def main():
    pierwsze_imie = str(input())
    drugie_imie = str(input())
    zostalo = {}
    x = []
    
    for i in drugie_imie:
        if i != "\n":
            if(i in zostalo):
                zostalo[i] += 1
            else:
                zostalo[i] = 1
        
        
    for i in pierwsze_imie:
        if i != "\n":
            if(i in zostalo and zostalo[i] > 0):
                zostalo[i] -= 1
                if(zostalo[i] == 0):
                    del zostalo[i]
            elif(i in zostalo and zostalo[i] == 0):
                del zostalo[i]       
            
            
            
    if len(zostalo) == 0:
        print("YES YES YES")
    else:
        for i in zostalo:
            for k in range(zostalo[i]):
                x.append(i)
        
        x.sort()
    
        for i in x:
            print(i, end = " ")
        
main()
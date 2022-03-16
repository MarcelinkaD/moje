from sys import stdin
input = stdin.readline

def main():
    lista = str(input())
    a = 0
    b = 0
    
    for i in lista:
        if i == "A":
            a += 1
        elif i == "B":
            b += 1
            
    print(str(a) + " : " + str(b))
    
main()
from sys import stdin
input = stdin.readline

def main():
    liczba_mew = int(input())
    mewy = list(map(int, input().split()))
    prze = []
    nie_prze = []
    for i in range(len(mewy)):
        if(mewy[i] % 400 == 0):
            print(mewy[i], end = " ")
        elif(mewy[i] % 4 == 0 and mewy[i] % 100 != 0):
            print(mewy[i], end = " ")
        else:
            nie_prze.append(mewy[i])
    
    for i in nie_prze:
        print(i, end = " ")
        
main()
from sys import stdin
input = stdin.readline

def main():
    liczba = str(input())
    k = 0
    
    for i in liczba:
        if i == "4" or i == "7":
            k += 1
            
    if k == 4 or k == 7:
        print("YES")
    else:
        print("NO")

main()
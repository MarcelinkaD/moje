from sys import stdin
input = stdin.readline

def main():
    liczby = list(map(int, input().split()))
    liczby.sort()
    
    naj = liczby[len(liczby) - 1]
    A = liczby[0]
    B = liczby[1]
    C = naj - (A + B)
    
    print(str(A), str(B), str(C))
       
    
main()
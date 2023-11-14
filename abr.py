# uwaga w zadaniu nas zkoepule sa bledne testy https://szkopul.edu.pl/problemset/problem/abraham/site/?key=statement
from sys import stdin
input = stdin.readline
    
def main():
    n, m = map(int, input().split())
    kolka = list(map(int, input().split()))
    kan = list(map(int, input().split()))
    w = 0
    i = 0
    k = 0
    kan.sort()
    kolka.sort()
    co = kolka[0]
    #breakpoint()
    
    while k != len(kan):
        if kan[k] > co:
            w += kan[k] - co
            i += 1
            if i == len(kolka):
                break
            co = kolka[i]
            
        k += 1
            
            
                
                
    if k == len(kan) - 1 and i != len(kolka):
        print("NIE")
    else:
        print("TAK")
        print(w)
            
            
        
        

    
    
    
main()


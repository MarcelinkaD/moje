from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))  
    l.sort()
    print(l[-1] - l[0])
    
main()
from sys import stdin
input = stdin.readline

def main():
    sett = set(map(str, input().split()))
    n = str(input().strip())
    
    if n in sett:
        print("SuPeR!")
    else:
        print("NiEeEeE:|")
    
main()
from sys import stdin
input = stdin.readline

def main():
    nikname = str(input())
    gb = set([])
    
    for i in nikname:
        gb.add(i)
        
    if len(gb) % 2 == 1:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

main()
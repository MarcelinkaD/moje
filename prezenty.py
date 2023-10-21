# https://szkopul.edu.pl/problemset/problem/krSKKe-crppvN2OV2aw1MUYm/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    pre = int(input())
    w = []
    
    if pre % 2 == 0:
        for i in range(pre // 2):
            w.append((2, i + 1, pre - i))
    else:
        for i in range(pre - 1, pre // 2, -1):
            w.append((2, pre - i, i))
        w.append((1, pre))
        
    print(len(w))
    
    for i in w:
        if len(i) == 3:
            print(i[0], i[1], i[2])
        else:
            print(i[0], i[1])
    
main()
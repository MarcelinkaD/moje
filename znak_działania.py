# https://szkopul.edu.pl/c/testowy_dd/p/zna/18795/

from sys import stdin
input = stdin.readline

def main():
    a, b = map(int, input().split())
    operacje = ["+", "-", "*"]
    ile_tak_sam = 0
    naj_w = -1e18
    znak = ""
    
    for op in operacje:
        if op == "+":
            w = a + b
        elif op == "-":
            w = a - b
        else:
            w = a * b
            
        if w > naj_w:
            naj_w = w
            znak = op
        elif w == naj_w:
            ile_tak_sam += 1
            
    if ile_tak_sam > 0:
        print("NIE")
    else:
        if a < 0:
            a = "(" + str(a) + ")"
            
        if b < 0:
            b = "(" + str(b) + ")"
            
        if naj_w < 0:
            naj_w = "(" + str(naj_w) + ")"
            
        a = str(a)
        b = str(b)
        naj_w = str(naj_w)
            
        print(a + znak + b + "=" + naj_w)
    
    
main()
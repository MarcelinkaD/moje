# https://sio2.mimuw.edu.pl/c/oij18-1/p/art/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    while n > 26:
        print("z", end = "")
        n -= 26
        
    print(alfa[n - 1])
    
main()
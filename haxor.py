# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/hax/

from sys import stdin
input = stdin.readline

def main():
    s = str(input().strip())
    susy = {"a" : "4", "e" : "3", "i" : "1", "o" : "0", "s" : "5"}
    
    for i in s:
        if i in susy:
            print(susy[i], end = "")
        else:
            print(i, end = "")
    
main()
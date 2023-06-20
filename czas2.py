# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/cza/25406/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    godz = n // 3600
    n -= godz * 3600
    min = n // 60
    n -= min * 60
    print(godz, end = "")
    print("g", end = "")
    print(min, end = "")
    print("m", end = "")
    print(n, end = "")
    print("s", end = "")
    
main()
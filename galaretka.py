# https://szkopul.edu.pl/problemset/problem/xiVR2jzH4FrgmSnOdFNQryN-/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
	n, h = map(int, input().split())
	l = list(map(int, input().split()))
	w = 0
	
	for i in range(n):
		if l[i] < h:
			h = l[i]
			w += 1
			
	print(w)
	
main()

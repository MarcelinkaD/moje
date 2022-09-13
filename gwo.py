from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	gwo = list(map(int, input().split()))
	c = C(gwo)
	co, ile = 0, 0
	gwo.sort()
	
	for i in c:
		if c[i] > ile:
			ile = c[i]
			co = i
			
	w = ile
	breakpoint()
	for i in range(n - k - 1, n):
		if gwo[i] > co:
			w += 1
			
	print(w)
	
main()

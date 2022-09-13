from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	c = C(l)

	for i in c:
		if c[i] == i:
			continue
		else:
			print("NIE")
			return 0
	
	print("TAK")
	
main()

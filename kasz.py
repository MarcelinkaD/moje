from itertools import accumulate
from sys import stdin
input = stdin.readline

def main():
	d = int(input())
	
	for i in range(d):
		l = list(map(int, input().split()))
		l.remove(l[0])
		ac = list(accumulate(l))
		print(ac[len(ac) - 1])
	
main()

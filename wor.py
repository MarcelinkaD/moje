import bisect
from collections import Counter as C
from sys import stdin
input = stdin.readline

def binary(li, n):
	o = bisect.bisect_left(li, n)
	if o != len(li) and li[o] == n:
		return o
	else:
		return -1

def main():
	n = int(input())
	l = list(map(int, input().split()))
	q = int(input())
	c = C(l)
	l.sort()
	for i in range(q):
		r = int(input())
		if binary(l, r) == -1:
			print(0)
		else:
			print(c[r])
	
main()


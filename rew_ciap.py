from itertools import accumulate
from sys import stdin
input = stdin.readline

def main():
	lm, q = map(int, input().split())
	przerwy = list(map(int, input().split()))
	pref = list(accumulate(przerwy))
	pref.insert(0, 0)
	
	for i in range(q):
		od, do = map(int, input().split())
		print(abs(pref[do - 1] - pref[od - 1]))
	
	
main()

from sys import stdin
input = stdin.readline
from itertools import accumulate

def main():
	n = int(input())
	wagony = list(map(int, input().split()))
	q = int(input())
	pref = list(accumulate(wagony))
	
	pref.insert(0, 0)
	
	for i in range(q):
		od, do = map(int, input().split())
		print(pref[do] - pref[od - 1])
	
main()

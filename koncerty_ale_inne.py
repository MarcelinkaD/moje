from sys import stdin
input = stdin.readline
from itertools import accumulate

def main():
	n = int(input())
	kon = list(map(int, input().split()))
	pref = list(accumulate(kon))
	pref.insert(0, 0)
	q = int(input())
	
	for i in range(q):
		od, do = map(int, input().split())
		print(pref[do] - pref[od - 1])
		
	
main()

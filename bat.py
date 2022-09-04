from itertools import accumulate
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	czesci = list(map(int, input().split()))
	max_wyn, akt_wyn = 0, 0
	for i in czesci:
		akt_wyn = max(akt_wyn + i, 0)
		max_wyn = max(akt_wyn, max_wyn)
	print(max_wyn)
	
main()

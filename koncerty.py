from sys import stdin
input = stdin.readline
from itertools import accumulate

def main():
	kon = int(input())
	wszystkiekoncerty = list(map(int, input().split()))
	sumypref = list(accumulate(wszystkiekoncerty))
	sumypref.insert(0, 0)
	ilepytan = int(input())

	for i in range(ilepytan):
		od, do = map(int, input().split())
		print(sumypref[do] - sumypref[od - 1])
		
main()

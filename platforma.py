# algorytm pochodzi z -https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

from heapq import heappush,heappop, heapify,_heapify_max
from sys import stdin
input = stdin.readline

def main():
	n, q = map(int, input().split())
	l = list(map(int, input().split()))

	median = 0
	# Declaring two min heap
	g = []
	s = []
	for i in range(len(l)):
	   
		
		heappush(s, -l[i])
		heappush(g, -heappop(s))
		if len(g) > len(s):
			heappush(s, -heappop(g))

		if len(g) != len(s):
			print(float(-s[0]))
		else:
			print((g[0] - s[0])/2.0)

			
main()

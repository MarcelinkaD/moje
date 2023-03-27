import bisect as bis
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	q = int(input())
	l.sort(reverse = True)
	pref = [0] * n 
	pref[0] = l[0]
	
	for i in range(1, n):
		pref[i] = pref[i - 1] + l[i]
		
		
	for _ in range(q):
		k = int(input())
		if n == 1:
			print(1)
		else:
			g = bis.bisect_left(pref, k)
			print(g + 1)
	
	
main()

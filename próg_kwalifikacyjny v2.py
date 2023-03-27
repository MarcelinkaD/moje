# https://szkopul.edu.pl/problemset/problem/1O7x62PkwWamYGZjSs_3McJe/site/?key=statement
import bisect as bi
from sys import stdin
input = stdin.readline	

def fast():
	n = int(input())
	l = list(map(int, input().split()))
	l.sort(reverse = True)
	pref = [0] * (n + 1)
	l.insert(0, 0)
	
	for i in range(1, n + 1):
		pref[i] = pref[i - 1] + l[i]
		

	q = int(input())
	
	for _ in range(q):
		pr = int(input())
		gdzie = bi.bisect_left(pref, pr)
		# ~ breakpoint()
		print(gdzie)
	
	
fast()

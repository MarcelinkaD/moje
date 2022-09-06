from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	kon = list(map(int, input().split()))
	ile_bylo = 0
	pref = list(ac(kon))
	mini = 222222222222222222222222222222222222
	pref.insert(0, 0)
	
	if k == n:
		print(pref[-1])
		return 0

	
	for i in range(k, n):
		mini = min(pref[i] - pref[i - k], mini)
	
	if mini == 222222222222222222222222222222222222:
		print(0)
	else:
		print(mini)
		
main()

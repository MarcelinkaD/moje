from sys import stdin
input = stdin.readline
from itertools import accumulate
import bisect

def main():
	licz = int(input())
	miasta = list(map(int, input().split()))
	miasta.insert(0, 0)
	pref = list(accumulate(miasta))
	maxi = pref[len(pref) - 1]
	szukam = maxi // 2
	mam = bisect.bisect_left(pref, szukam)
	breakpoint()
	if pref[mam] == szukam:
		return mam + 1
	else:
		prawo = pref[mam + 1]
		lewo = pref[mam - 1]
		
		if abs(prawo - szukam) < abs(szukam - lewo):
			return mam + 2
		elif abs(prawo - szukam) > abs(szukam - lewo):
			return mam + 1
		else:
			return str(mam - 1) + " " + str(mam + 1)
	
	
print(main())

import bisect as b
from sys import stdin
input = stdin.readline

def binary_git_kolejnosc(li, n):
	g = b.bisect_left(li, n)
	if g != len(li) and li[g] == n:
		return "TAK"
	else:
		return "NIE"
	

def binary_nie_git_kolejnosc(li, n):
	pocz = 0
	kon = len(li)
	while pocz < kon:
		srodek = (pocz + kon) // 2
		if li[srodek] == n:
			return "TAK"
		elif li[srodek] > n:
			pocz = srodek + 1
		else:
			kon = srodek
			
	if pocz == kon and li[kon] == n:
		return "TAK"

	return "NIE"
	

def main():
	n, k = map(int, input().split())
	co = str(input().strip())
	l = list(map(int, input().split()))

	if co == "mal":
		print(binary_nie_git_kolejnosc(l, k))
	else:
		print(binary_git_kolejnosc(l, k))
	
	
main()

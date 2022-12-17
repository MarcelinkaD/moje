from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	tab = list(map(int, input().split()))
	tab.insert(0, 0)
	pref = [0] * (n + 1)
	
	for i in range(1, n + 1):
		if i != 1 and i != n:
			if tab[i] > tab[i - 1] and tab[i] > tab[i + 1]:
				pref[i] = 1 + pref[i - 1]
			else:
				pref[i] = pref[i - 1]
		else:
			pref[i] = pref[i - 1]
			
	pref.remove(0)
	q = int(input())
		
	for i in range(q):
		od, do = map(int, input().split())
		print(pref[do] - pref[od])

		
		
main()

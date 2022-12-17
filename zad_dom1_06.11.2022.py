from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	tab = list(map(int, input().split()))
	tab.insert(0, 0)
	pref = [0] * (n + 1)
	
	for i in range(1, n + 1):
		pref[i] = pref[i - 1] + tab[i]
		
	wyn = 1e6
	for i in range(1, n + 1):
		w1 = pref[i] 
		w2 = pref[n] - pref[i]
		
		if wyn > abs(w2 - w1):
			wyn = w2 - w1
			
	print(wyn)
			
	
main()

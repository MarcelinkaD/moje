from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	parz = 0
	nieparz = 0
	w = 0
	l.insert(0, 0)
	pref = [0] * (n + 1)
	
	for i in range(1, n + 1):
		pref[i] = pref[i - 1] + l[i]
	
	for i in range(n + 1):
		if pref[i] % 2 == 0:
			w += parz
			parz += 1
		else:
			w += nieparz
			nieparz += 1
			
	print(w)
	
main()





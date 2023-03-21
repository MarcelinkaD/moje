from sys import stdin
input = stdin.readline

def main():
	MAXN = 1000000007
	n = int(input())
	l = list(map(int, input().split()))
	pref = [1] * (n)
	pref_odwr = [1] * n
	pref_odwr[-1] = l[-1]
	pref[0] = l[0]
	
	for i in range(1, n):
		pref[i] = (pref[i - 1] * l[i]) % MAXN
		
	for i in range(n - 2, -1, -1):
		pref_odwr[i] = (pref_odwr[i + 1] * l[i]) % MAXN
		
	
	for i in range(n):
		if i == 0:
			wynik = pref_odwr[i + 1]
		elif i == n - 1:
			wynik = pref[i - 1]
		else:
			wynik = (pref[i - 1] * pref_odwr[i + 1]) % MAXN
			
		print(wynik, end = " ")
			
	
	
main()



from sys import stdin
input = stdin.readline

def main():
	ilosc_liczb, q = map(int, input().split())
	liczby = list(map(int, input().split()))
	liczby.insert(0,0)
	pref = [0] * (ilosc_liczb + 1)
	pref[0] = liczby[0]
	
	for i in range(1, ilosc_liczb + 1):
		pref[i] = liczby[i] + pref[i - 1]
		
	# breakpoint()
	
	for i in range(q):
		od, do = map(int, input().split())
		print((pref[do] - pref[0]) - (pref[od - 1] - pref[0]))

main()

from sys import stdin
input = stdin.readline

def main(args):
	dnie, liczba_miast, liczba_zapytan = map(int, input().split())
	miasta = [0 for i in range(liczba_miast + 1)]
	pref = [0] * (liczba_miast + 1)

	for i in range(1, dnie + 1):
		od, do, ile = map(int, input().split())
		miasta[od] += ile
		if do + 1 <= liczba_miast:
			miasta[do + 1] -= ile
	
	
		
	for i in range(1, liczba_miast + 1):
		pref[i] = miasta[i] + pref[i - 1]
		
	for c in range(liczba_zapytan):
		z = int(input())
		print(pref[z])
	


if __name__ == '__main__':
    import sys
    main(sys.argv)

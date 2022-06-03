from sys import stdin
input = stdin.readline

def main(args):
	liczba_glajd = int(input())
	gracze = list(map(int, input().split()))
	gracze.sort()
	wynik = 0
	bajtek = 2
	naj = max(gracze)
	
	for i in gracze:
		if bajtek >= naj:
			print(wynik)
			return ""
		if bajtek > i:
			bajtek += i
			wynik += 1
		else:
			print("NIE")
			return ""
	
	print(wynik)
	return ""

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

from sys import stdin
input = stdin.readline

def potega(a, b, M):
	if b == 0:
		return 1
		
	wynik = potega(a, b // 2, M)
	wynik = (wynik * wynik) % M
	
	if b % 2 == 1:
		wynik = (wynik * a) % M
	return wynik


def main():
	q = int(input())
	
	for i in range(q):
		a, b = map(int, input().split())
		print(potega(a + 1, b, 10000))
	
main()

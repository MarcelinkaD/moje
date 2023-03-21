from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	lista_wag = list(map(int, input().split()))
	q = int(input())
	lista_wag.insert(0, 0)
	
	for _ in range(q):
		od, do = map(int, input().split())
		print(lista_wag[do] - lista_wag[od - 1])
	
main()

from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	wie = [set() for i in range(n + 1)]
	
	for para in range(m):
		ten_pierwszy, ten_drugi = map(int, input().split())
		wie[ten_pierwszy].add(ten_drugi)
		wie[ten_drugi].add(ten_pierwszy)
		
		
	q = int(input())
	for i in range(q):
		pie, dru = map(int, input().split())
		if dru in wie[pie]:
			print("TAK")
		else:
			print("NIE")
	
main()

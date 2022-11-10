from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	
	while k > 0:
		reszta = n % k
		n, k = k, reszta
		
	print(n)
		
	
main()

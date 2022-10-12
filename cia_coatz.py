from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	
	while n != 1:
		if n % 2 == 0:
			print(n // 2, end = " ")
			n = n // 2
		else:
			n = n * 3 + 1
			print(n, end = " ")
	
main()

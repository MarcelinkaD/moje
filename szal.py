from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	if n % 2 == 0:
		print((n * n) // 2)
		print((n * n) // 2)
	else:
		print((n * n) // 2)
		print((n * n) // 2 + 1)
main()

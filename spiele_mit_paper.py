from sys import stdin
input = stdin.readline

def main():
	a, b = map(int, input().split())
	w = 0
	while b != 0:
		w += a // b
		a = a % b
		a, b = b, a
		
	print(w)
		
main()


from sys import stdin
input = stdin.readline

def main():
	l = 2
	w = 1
	x = int(input())

	while x >= l:
		l = 2 * l
		w += 1
	
	print(w)
	
main()

from sys import stdin
input = stdin.readline

def main():
	l1, l2 = map(int, input().split())
	if l1 == 1:
		print(l2 * l2)
	else:
		l3 = l2 // l1
		print(l3 * l2)
		
main()

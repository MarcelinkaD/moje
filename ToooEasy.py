from sys import stdin
input = stdin.readline

def main():
	l = list(map(int, input().split()))
	l.sort()
	
	for i in l:
		print(i, end = " ")

main()

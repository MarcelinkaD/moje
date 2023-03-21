from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	print(l[0], end = " ")
	
	for i in range(1, n):
		print(l[i] - l[i - 1], end = " ")
	
	
	
main()

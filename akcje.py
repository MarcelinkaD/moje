from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	naj_w = -1e4
	
	for i in range(n):
		for j in range(i, n):
			naj_w = max(naj_w, l[j] - l[i])
			
		
	print(naj_w)
		
	
main()

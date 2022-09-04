from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	w = [0] * k
	
	for i in range(1, n + 1):
		for v in range(0, k, i):
			w[v] += 1
			
	
	for i in w:
		print(i, end = " ")
	
	 
main()

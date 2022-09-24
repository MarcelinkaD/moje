from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	sk = []
	wy = 0
	
	for i in range(n):
		wiersz = list(map(int, input().split()))
		sk.append(wiersz)
		
	for i in range(m):
		mini = 1111111111111111111
		for k in range(n):
			if mini > sk[k][i]:
				mini = sk[k][i]
				
		wy += mini
		
	print(wy)
	
main()

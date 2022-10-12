from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	cz = list(map(int, input().split()))
	w = 0
	# ~ breakpoint()
	for i in range(n - 1, -1, -1):
		for h in range(i - 1, -1, -1):
			if abs(cz[i] - cz[h]) < k or abs(cz[i] - cz[h]) == k:
				w += k
			else:
				w += abs(cz[i] - cz[h])
				
	print(w)
	
main()

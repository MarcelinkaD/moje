from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	w = [h for h in range(n + 1)]
	k = [h for h in range(n + 1)]
	
	for v in range(m):
		li, a, b = map(str, input().split())
		a, b = int(a), int(b)
		# ~ breakpoint()
		if li == "K":
			s = k[a]
			k[a] = k[b]
			k[b] = s
		elif li == "W":
			s = w[a]
			w[a] = w[b]
			w[b] = s
		else:
			i, j = w[a], k[b]
			print((i - 1) * n + j)
	
main()
D

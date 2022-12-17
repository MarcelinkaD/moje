from sys import stdin
input = stdin.readline

def suma(i1, j1, i2, j2, sumy):
	return sumy[i2][j2] - sumy[i1 - 1][j2] - sumy[i2][j1 - 1] + sumy[i1 - 1][j1 - 1]
	

def main():
	n, r = map(int, input().split())
	l = [[0 for _ in range(n + 1)]]
	pref = [[0 for j in range(n + 1)] for i in range(n + 1)]
	for _ in range(n):
		linia = list(map(int, input().split()))
		linia.insert(0, 0)
		l.append(linia)
	
	
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + l[i][j]
	
	# ~ breakpoint()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			w = suma(max(1, i - r), max(1, j - r), min(n, i + r), min(n, j + r), pref)
			print(w, end = " ")
		print("")

main()

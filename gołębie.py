from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	l = [0] * 9000
	w = 0
	for _ in range(n):
		wyraz = str(input())
		akt = 0
		for j in range(k):
			if wyraz[j] == "1":
				akt += (1 << (k - j - 1))
				
		l[akt] += 1
		
	for i in range((1 << k) + 1):
		for j in range(i, (1 << k) + 1):
			if i & j != 0:
				if i == j:
					w += (l[i] * (l[i] - 1)) / 2
				else:
					w += l[i] * l[j]
					
	print(int(w))
	
main()

from sys import stdin
input = stdin.readline

def main():
	MAXN = int(1e6+4)
	sito = [0, 1] * (MAXN//2) + [1]
	sito[1], sito[2] = 0, 1
		
	for i in range(3, int(MAXN**0.5+1), 2):
		if sito[i] == 1:
			sito[i*i::2*i] = [0] * int((MAXN+2*i-1-i*i)/(2*i))
	
	n, k = map(int, input().split())
	dziel = []
	
	if k == 1:
		print(n)
		return 0
	
	d = 2
	while d * d <= n:
		while n % d == 0 and sito[d] == 1:
			dziel.append(d)
			n //= d
			k -= 1
			
			if k == 1:
				if n != 1:
					dziel.append(n)
				else:
					print(-1)
					return 0
				
				for i in dziel:
					print(i, end = " ")
					
				return 0
			
		d += 1
	
	print(-1)
	
	
main()


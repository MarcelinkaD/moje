from sys import stdin
input = stdin.readline

def binary(p, q):
	lewo = 1
	prawo = q
	
	while lewo < prawo:
		srodek = (lewo + prawo) // 2
		if srodek ** 3 + p * srodek == q:
			return srodek
		if srodek ** 3 + p * srodek <= q:
			lewo = srodek + 1
		else:
			prawo = srodek 
			
	return "NIE"
		

def main():
	n = int(input())
	
	for i in range(n):
		p, q = map(int, input().split())
		print(binary(p, q))
	
main()



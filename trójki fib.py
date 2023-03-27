from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	w = 0
	fib = [] 
	l1, l2 = 1, 1
	fib.append(0)
	fib.append(1)
	
	while l1 + l2 <= 10 ** 9:
		fib.append(l1 + l2)
		temp = l1 + l2
		l1 = l2 
		l2 = temp
		
	ile_fib = len(fib)
	zlicz = [0] * ile_fib
	prawo = [0] * n
	
	for i in range(n - 1, -1, -1):
		for j in range(ile_fib - 1, -1, -1):
			if fib[j] == l[i]:
				zlicz[j] += 1
			if fib[j] <= l[i]:
					break
		prawo[i] += zlicz[j]
		
	zlicz = [0] * ile_fib
	wynik = 0
	
	for i in range(n):
		lewo = 0
		for j in range(ile_fib):
			if fib[j] == l[i]:
				zlicz[j] += 1
			if fib[j] >= l[i]:
				break
		lewo += zlicz[j]
		wynik += lewo * prawo[i]
	print(wynik)
	
main()

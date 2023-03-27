from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	ile_ma = 0
	
	for i in range(n):
		ile_ma += 2 ** l[i] 
		
	w = 1
	
	while ile_ma >= 2 ** w:
		w += 1
	
	print(w - 1)
	
main()

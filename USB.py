import bisect as bi
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	m = int(input())
	l = []
	
	for _ in range(n):
		q = int(input())
		l.append(q)
		
	l.sort(reverse = True)
	w = 0
	
	for i in range(n):
		m -= l[i]
		w += 1
		
		if m <= 0:
			print(w)
			break
	
	
	
main()


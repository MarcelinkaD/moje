from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = sorted(list(map(int, input().split())))
	w = 0
	c = n - 1

	while c >= 2:
		a = 0
		b = c - 1
		while a < b:
			if l[a] + l[b] > l[c]:
				w += b - a
				b -= 1
			else:
				a += 1
			
		c -= 1
		  
	print(w)
		
	  
main()

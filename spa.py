from sys import stdin
input = stdin.readline
    
def main():
	q = int(input())
	
	for _ in range(q):
		z, do = map(int, input().split())
		w = 0
		
		while z != do:
			if do > z:
				do //= 2
				w += 1
			else:
				z //= 2
				w += 1
			
		print(w)
		
	
main()

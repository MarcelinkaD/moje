from sys import stdin
input = stdin.readline

def main():
	a, b = map(int, input().split())
	w = 0
	
	for i in range(a, b + 1):
		if i % 3 == 0 or i % 5 == 0:
			w += 1
			
	print(w)
	
main()

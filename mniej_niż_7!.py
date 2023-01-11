from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	w = 0
	
	for i in l:
		if i < 7:
			w += 1
			
	print(w)
	
main()

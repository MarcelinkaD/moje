from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	wk = ""
	
	for i in range(n + 2):
		wk += "#"
	
	print(wk)
	
	w = "#"
	
	for i in range(n):
		w += "@"
		
	w += "#"
	
	print(w)
	print(wk)
	
main()

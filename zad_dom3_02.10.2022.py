from sys import stdin
input = stdin.readline

def main():
	ma = str(input().strip())
	s = str(input().strip())
	di = {}
	w = ""
	alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
	
	for i in range(len(ma)):
		di[alfa[i]] = ma[i]
		
	for i in s:
		w += di[i]
		
	print(w)
		
	
main()

from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	g = ("+-" * len(s)) + "+"
	w = ""
	
	for i in s:
		w += "|" + i
		
	w += "|"
	
	print(g)
	print(w)
	print(g)
	
main()

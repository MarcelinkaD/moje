from sys import stdin
input = stdin.readline

def main():
	s = str(input())
	w = 0
	
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			w += 1
		
	print(w)
	
main()

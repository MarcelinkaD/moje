from sys import stdin
input = stdin.readline

def czy_pal(s):
	s = str(s)
	w = ""
	
	for i in range(len(s) - 1, -1, -1):
		w += s[i]
		
	if w == s:
		return True
	else:
		return False

def main():
	n = int(input())
	w = 0
	
	while True:
		if czy_pal(n) == True:
			print(w)
			return 0
		w += 1
		n += 1
	
	
main()

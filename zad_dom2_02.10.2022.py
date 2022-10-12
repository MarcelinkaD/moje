from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	w = ""
	dl = len(s)
	wys = dl // 3
	reszta = dl % 3
	l = [0 for i in range(dl)]
	i = 0
	
	while sum(l) != dl:
		if l[i] == 0:
			l[i] = 1
			w += s[i]
		i += 8
		if i >= dl:
			i = i - dl 
			
	print(w)
	
	
	
main()

from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	l.sort()
	w = 0
	glowa = 1
	ogon = 0
	pie = l[ogon] 
	dru = l[ogon + 1]
	trzy = l[glowa]
	breakpoint()
	
	if pie + dru > trzy:
			w += 1
			
	while ogon < n - 2:
		while glowa < n - 1 and pie + dru > trzy:
			glowa += 1
			trzy = l[glowa]
			
			if pie + dru > trzy:
				w += 1
			
		ogon += 1
		pie = l[ogon] 
		dru = l[ogon + 1]
		
		if pie + dru > trzy:
			w += 1
		
	print(w)
	
main()

from sys import stdin
input = stdin.readline
 
def f(li):
	for i in li:
		if i > 1:
			return False
			
	return True 
 
 
def main():
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	zlicz = [0] * (k + 1)
	glowa = -1
	ogon = 0
	w = 0
	
	while ogon < n - 1:
		while glowa < n - 1 and f(zlicz):
			glowa += 1
			zlicz[l[glowa]] += 1
			
			if glowa == ogon:
				w += 1
				continue
				
			if f(zlicz):
				w += 2
			else:
				break
				
		zlicz[l[ogon]] -= 1
		ogon += 1
		
		if f(zlicz):
			w += 1
			
	print(w)

main()

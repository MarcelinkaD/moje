from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	l1, l2 = map(int, input().split())
	w1 = str(input().strip())
	w2 = str(input().strip())
	zlicz_pop = C(w2)
	
	glowa = l2 - 1
	ogon = 0
	
	zlicz_akt = dict(C(w1[ogon : glowa + 1]))
	wyn = []
	# ~ breakpoint()
	while glowa < l1 - 1:
		if zlicz_akt == zlicz_pop:
			wyn.append(ogon + 1)
			
		glowa += 1
		if w1[glowa] in zlicz_akt:
			zlicz_akt[w1[glowa]] += 1
		else:
			zlicz_akt[w1[glowa]] = 1
			
		zlicz_akt[w1[ogon]] -= 1
		if zlicz_akt[w1[ogon]] == 0:
			del zlicz_akt[w1[ogon]]
			
		ogon += 1
		
		
	if zlicz_akt == zlicz_pop:
		wyn.append(ogon + 1)
		
	print(len(wyn))
	
	for i in wyn:
		print(i, end = " ")
	
main()

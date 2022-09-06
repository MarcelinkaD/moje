from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	li = list(map(int, input().split()))
	glowa = -1
	ogon = 0
	akt_wyn = 0
	max_wyn = 777777777777777777777
	tk = 0
	licz_kap = 0
	licz_roz = 0

	
	while ogon < n - 1:
		while glowa < n - 1 and licz_roz < k:
			glowa += 1
			if li[glowa] == 1:
				licz_roz += 1
			else:
				licz_kap += 1
				akt_wyn = licz_kap
				
			if licz_roz >= k:
				max_wyn = min(licz_kap, max_wyn)
			
		if li[ogon] == 1:
			licz_roz -= 1
		else:
			licz_kap -= 1
		
		if licz_roz >= k:
				max_wyn = min(licz_kap, max_wyn)
				
		ogon += 1
	
	if max_wyn == 777777777777777777777:
		print("NIE")
	else:
		print(max_wyn)
		
main()

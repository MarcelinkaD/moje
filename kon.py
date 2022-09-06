from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	kon = list(map(int, input().split()))
	glowa = -1
	ogon = 0
	akt_wyn = 0
	min_wyn = 9999999999999999999999999999999999999
	uk = 0

	while ogon < n - 1:
		while glowa < n - 1 and uk < k:
			glowa += 1
			akt_wyn += kon[glowa]
			uk += 1
			
			if uk == k:
				min_wyn = min(min_wyn, akt_wyn)
		
		
		akt_wyn -= kon[ogon]
		uk -= 1
		ogon += 1
		if uk == k:
			min_wyn = min(min_wyn, akt_wyn)
	
	if min_wyn == 9999999999999999999999999999999999999:
		print(0)
	else:
		print(min_wyn)
	
main()

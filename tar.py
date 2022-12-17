from sys import stdin
input = stdin.readline

def gasienica(tarasy, k, n):
	glowa = -1
	ogon = 0
	naj_wyn = -1
	akt_wyn = 0
	akt_kre = k
	
	while ogon < n - 1:
		while glowa < n - 1 and akt_kre >= 0:
			glowa += 1
			akt_kre -= tarasy[glowa]
			
			if akt_kre >= 0:
				akt_wyn += 1
			else:
				break
			
			
			naj_wyn = max(naj_wyn, akt_wyn)
			
		akt_kre += tarasy[ogon]
		ogon += 1
		akt_wyn -= 1
		naj_wyn = max(naj_wyn, akt_wyn)
		
	return naj_wyn

def main():
	n, k = map(int, input().split())
	ntar = [0] * n
	tarasy = []
	
	for i in range(n):
		tarasy.append(int(input()))
	
	for i in range(n - 1, 0, -1):
		if tarasy[i] > tarasy[i - 1]:
			ntar[i] = tarasy[i] - tarasy[i - 1]
		else:
			ntar[i] = 0
	
	tarasy.reverse()
	for i in range(n - 1, 0, -1):
		if tarasy[i] > tarasy[i - 1]:
			tarasy[i] = tarasy[i] - tarasy[i - 1]
		else:
			tarasy[i] = 0
			
	tarasy[0] = 0
	ntar[0] = 0
	pie = gasienica(ntar, k, n)
	dru = gasienica(tarasy, k, n)
	
	print(max(pie, dru))

	
main()

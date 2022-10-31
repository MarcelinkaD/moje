from sys import stdin
input = stdin.readline
    
def main():
	liczba_wagonow, suma = map(int, input().split())
	wagony = list(map(int, input().split()))
	naj_wynik = 68543675467586749856
	akt_wynik = 0
	glowa = -1
	ogon = 0
	
	if suma in wagony:
		return 1
	
	while ogon < liczba_wagonow - 1:
		while glowa < liczba_wagonow - 1 and akt_wynik <= suma:
			# ~ breakpoint()
			glowa += 1
			akt_wynik += wagony[glowa]
			
			if akt_wynik == suma:
				naj_wynik = min(naj_wynik, glowa - ogon + 1)
				
		akt_wynik -= wagony[ogon]
		ogon += 1
		
		if akt_wynik == suma:
			naj_wynik = min(naj_wynik, glowa - ogon + 1)
			
	if naj_wynik == 68543675467586749856:
		return "N"
	else:
		return naj_wynik
	
	 

print(main())

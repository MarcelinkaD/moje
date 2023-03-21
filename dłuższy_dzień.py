from sys import stdin
input = stdin.readline

def main():
	dzien, miesiac = map(str, input().split())
	orgdz, orgmies = dzien, miesiac
	dzien = int(dzien)
	if dzien == 21 and miesiac == "czerwiec":
		print("NOC SWIETOJANSKA!")
		return 0
		
	maximum_dni = {"styczen" : 31, "luty" : 29, "marzec" : 31, "kwiecien" : 30, "maj" : 31, "czerwiec" : 30, "lipiec" : 31, "sierpien" : 31, "wrzesien" : 30, "pazdziernik" : 31, "listopad" : 30, "grudzien" : 31}
	miesiace = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
	index_miesiaca = miesiace.index(miesiac)
	lddd = 0
	
	if miesiac == "styczen" or miesiac == "luty" or miesiac == "marzec" or miesiac == "kwiecien" or miesiac == "maj" or (dzien < 21 and miesiac == "czerwiec") or (dzien > 21 and miesiac == "grudzien"):
		dzien += 1
		if maximum_dni[miesiac] < dzien:
			dzien = 1
			if miesiac == "styczen":
				miesiac = "luty"
			elif miesiac == "luty":
				miesiac = "marzec"
			elif miesiac == "marzec":
				miesiac = "kwiecien"
			elif miesiac == "kwiecien":
				miesiac = "maj"
			elif miesiac == "maj":
				miesiac = "czerwiec"
			elif miesiac == "grudzien":
				miesiac = "styczen"				
				
			#dodac czerwiec ale tylko do 21 
				
		print(str(dzien), miesiac)
		
	else:
		
		if miesiac != "grudzien":
			lddd = maximum_dni[miesiac] - dzien + 1
			dzien = 1
			index_miesiaca += 1
			miesiac = miesiace[index_miesiaca]
		# ~ breakpoint()
		while miesiac != "grudzien":
			index_miesiaca += 1
			lddd += maximum_dni[miesiac]
			miesiac = miesiace[index_miesiaca]
		
		
		lddd += 21 - dzien 
		#breakpoint()
		
		dzien = 22
		index_miesiaca = -1
		dzien += lddd
		
		
		while dzien > maximum_dni[miesiac]:
			index_miesiaca += 1
			dzien -= maximum_dni[miesiac]
			miesiac = miesiace[index_miesiaca]
		
		
		print(str(dzien), miesiac)

	
main()

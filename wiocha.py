from itertools import product
from sys import stdin
input = stdin.readline

def czy_elf(czy_noc, wypowiedź, osoba):
	if osoba == "ja":
		if wypowiedź.endswith("Jestem elfem.") and czy_noc == False:
			return True
		elif wypowiedź.endswith("Jestem elfem.") and czy_noc:
			return False
		elif wypowiedź.endswith("Jestem orkiem.") and czy_noc:
			return True
		elif wypowiedź.endswith("Jestem orkiem.") and czy_noc == False:
			return False
		elif wypowiedź.endswith("Jestem krasnoludem.") and czy_noc == False:
			return False
		elif wypowiedź.endswith("Jestem krasnoludem.") and czy_noc:
			return True
	else:
		if wypowiedź.endswith("jest elfem.") and czy_noc:
			return not osoba == "E"
		elif wypowiedź.endswith("jest elfem.") and czy_noc == False:
			return osoba == "E"
		
		if wypowiedź.endswith("jest krasnoludem."):
			if czy_noc:
				return not osoba == "K"
			else:
				return osoba == "K"
				
		if wypowiedź.endswith("jest orkiem."):
			if czy_noc:
				return not osoba == "O"
			else:
				return osoba == "O"
				
def czy_kras(wypowiedź, osoba):
	if osoba == "ja":
		if wypowiedź.endswith("Jestem krasnoludem."):
			return True
		else:
			return False
	else:
		if wypowiedź.endswith("jest elfem."):
			return osoba == "E"
		elif wypowiedź.endswith("jest krasnoludem."):
			return osoba == "K"
		elif wypowiedź.endswith("jest orkiem."):
			return osoba == "O"
		

def czy_ork(wypowiedź, osoba):
	if osoba == "ja":
		if wypowiedź.endswith("Jestem orkiem."):
			return False
		else:
			return True
	else:
		if wypowiedź.endswith("jest elfem."):
			return not osoba == "E"
		elif wypowiedź.endswith("jest krasnoludem."):
			return not osoba == "K"
		elif wypowiedź.endswith("jest orkiem."):
			return not osoba == "O"
  
def odmien(o):
	if o == "K":
		return "krasnoludem."
	elif o == "O":
		return "orkiem."
	else:
		return "elfem." 

def sprawdz(ind, li):
	pop = li[0][ind]
	for c in li:
		if c[ind] == pop:
			pop = c[ind]
		else:
			return False
			
	return True
   
def main():
	liczba_ziomkow, lwyp = map(int, input().split())
	ziomki = list(map(str, input().split()))
	wypowiedzi = []
	kombinacje = []
	dobre_kom = []
	
	for _ in range(lwyp):
		f = str(input().strip())
		wypowiedzi.append(f)
		
	
	for kombinacja in product(["E","O","K"], repeat=liczba_ziomkow):
		kombinacje.append(kombinacja)
	# ~ breakpoint()
	for kombinacja in kombinacje:
		strefa = ""
		dobra_kom = True
		for wyp in wypowiedzi:
			indx = wyp.index(":")
			os_mowiaca = wyp[0 : indx]
			index_podmiotu_lirycznego = ziomki.index(os_mowiaca)
			kim_jest_pod_lir = kombinacja[index_podmiotu_lirycznego]
			
			if wyp.find("Jestem") != -1:
				kim_jest_przed_wyp = "ja"
			else:
				przedmiot_wyp = wyp.split()[1]
				index_przedmiot_wyp = ziomki.index(przedmiot_wyp)
				kim_jest_przed_wyp = kombinacja[index_przedmiot_wyp]
			# ~ breakpoint()
			if kim_jest_pod_lir == "O":
				odp = czy_ork(wyp, kim_jest_przed_wyp)
				if odp == False:
					dobra_kom = False
					break
			elif kim_jest_pod_lir == "K":
				odp = czy_kras(wyp, kim_jest_przed_wyp)
				if odp == False:
					dobra_kom = False
					break
			else:
				odp1 = czy_elf(False, wyp, kim_jest_przed_wyp)
				odp2 = czy_elf(True, wyp, kim_jest_przed_wyp)
				if odp1 == False and odp2 == False:
					dobra_kom = False
					break
				elif odp1 == True and odp2 == False and strefa != "Noc":
					stefa = "Dzień"
				elif odp1 == False and odp2 == True and strefa != "Dzień":
					strefa = "Noc"
				else:
					dobra_kom = False
					break
					
		if dobra_kom:
			dobre_kom.append(kombinacja)
			
	# ~ breakpoint()
	if len(dobre_kom) == 1:
		for i in dobre_kom:
			for k in range(liczba_ziomkow):
				print(ziomki[k], end = " ")
				print("jest", end = " ")
				print(odmien(i[k]))
	else:
		czy_wypisalam = False
		for i in range(liczba_ziomkow):
			if sprawdz(i, dobre_kom):
				czy_wypisalam = True
				print(ziomki[i], end = " ")
				print("jest", end = " ")
				print(odmien(dobre_kom[0][i]))
		
		if czy_wypisalam == False:
			print("Nic nie wiadomo!")
				
	
main()










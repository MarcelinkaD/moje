from sys import stdin
input = stdin.readline
    
def czy_elf(czy_noc, wypowiedź, osoba):
	# ~ breakpoint()
	if osoba == "ja":
		if wypowiedź == "Jestem elfem." and czy_noc == False:
			return True
		elif wypowiedź == "Jestem elfem." and czy_noc:
			return False
		elif wypowiedź == "Jestem orkiem." and czy_noc:
			return True
		elif wypowiedź == "Jestem orkiem." and czy_noc == False:
			return False
		elif wypowiedź == "Jestem krasnoludem." and czy_noc == False:
			return False
		elif wypowiedź == "Jestem krasnoludem." and czy_noc:
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
		


def main():
	w = str(input().strip())
	os = str(input().strip())
	noc = str(input().strip())
	
	if noc == "Tak":
		print(czy_elf(True, w, os))
	else:
		print(czy_elf(False, w, os))
	
main()

from sys import stdin
input = stdin.readline
    
def czy_kras(czy_noc, wypowiedź, osoba):
	# ~ breakpoint()
	if osoba == "ja":
		if wypowiedź == "Jestem krasnoludem.":
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
		



def main():
	w = str(input().strip())
	os = str(input().strip())
	noc = str(input().strip())
	
	if noc == "Tak":
		print(czy_kras(True, w, os))
	else:
		print(czy_kras(False, w, os))
	
main()

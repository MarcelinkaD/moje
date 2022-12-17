from sys import stdin
input = stdin.readline
    
def czy_ork(czy_noc, wypowiedź, osoba):
	# ~ breakpoint()
	if osoba == "ja":
		if wypowiedź == "Jestem orkiem.":
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
		



def main():
	w = str(input().strip())
	os = str(input().strip())
	noc = str(input().strip())
	
	if noc == "Tak":
		print(czy_ork(True, w, os))
	else:
		print(czy_ork(False, w, os))
	
main()


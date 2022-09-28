from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	w = ""
	oij = [0, 0, 0]
	ejoi = [0, 0, 0, 0]
	ioi = [0, 0, 0]
	czybylo = False
	# ~ breakpoint()
	for i in s:
		if i == "O":
			oij[0] = 1
			ejoi[2] = 1
			ioi[1] = 1
		elif i == "E":
			ejoi[0] = 1
		elif i == "J":
			oij[2] = 1
			ejoi[1] = 1
		elif i == "I" and czybylo == False:
			oij[1] = 1
			ejoi[3] = 1
			ioi[0] = 1
			czybylo = True
		elif i == "I" and czybylo == True:
			ioi[2] = 1
			
	if sum(oij) == 3:
		w += "T"
	else:
		w += "N"
	
	if sum(ejoi) == 4:
		w += "T"
	else:
		w += "N"
		
	if sum(ioi) == 3:
		w += "T"
	else:
		w += "N"
		
	print(w)
	
	
main()

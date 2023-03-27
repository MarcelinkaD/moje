from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	l1, l2 = s[0], s[1]
	
	if l1 == l2:
		print("NIE")
		return 0
		
	kto_teraz = 1
	w = True
	
	for i in range(len(s)):
		if kto_teraz == 1:
			if s[i] != l1:
				print("NIE")
				return 0
			kto_teraz = 2
		else:
			if s[i] != l2:
				print("NIE")
				return 0
			kto_teraz = 1
			
	print("TAK")
	
main()

from sys import stdin
input = stdin.readline

def gra():
	import random
	l = random.randint(1, 100)
	liczba_rochow = 7
	
	while liczba_rochow != 0:
		print("Podaj liczbę od 1 do 100")
		gracz = int(input())
		liczba_rochow -= 1
		if l < gracz:
			print("Za duża")
			print("")
		elif l > gracz:
			print("Za mała")
			print("")
		else:
			print("Brawo! Liczba ruchów: " + str((7 - liczba_rochow)))
			return 0
	
	print("Przekroczony limit ruchów :C")
	print("Poprawna odpowiedź to: " + str(l))
	
gra()

from sys import stdin
input = stdin.readline

def pierwiastek(x):
	if x == 0 or x == 1:
		return x
	
	lewo = 1
	prawo = x // 2
	while lewo <= prawo:
		sro = (lewo + prawo) // 2
		if sro * sro == x:
			return sro
		
		if sro * sro < x:
			lewo = sro + 1
			wyn = sro
		else:
			prawo = sro - 1
			
	return wyn

def main():
	n = int(input())
	pie = pierwiastek(n)
	
	print(pie + 1)
	
main()

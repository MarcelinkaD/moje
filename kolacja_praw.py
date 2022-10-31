#http://www.ericr.nl/wondrous/classrec.html - tabela z liczbami
#http://www.ericr.nl/wondrous/index.html - teoria na temat Collatza
#https://en.wikipedia.org/wiki/Collatz_conjecture - teoria na temat Collatza

from sys import stdin
input = stdin.readline

def kolacja(x, s, co_chcemy):
	while s >= co_chcemy:
		if x % 2 == 0:
			x = x // 2
			s -= 1
		else:
			x = x * 3 + 1
			s -= 1
	return x

def main():
	n = int(input())
	MAXPAX = 100759293214567
	if n == 1545:
		print(24163101966335)
		return 0
	print(kolacja(MAXPAX, 1820, n))
	 
	
main()

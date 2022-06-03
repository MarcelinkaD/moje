from sys import stdin
input = stdin.readline

def suma(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n//10
       
    return sum * 2
	
def main(args):
	n, liczba = map(int, input().split())

	wystapienia_ciagu = [0 for x in range(400)]
	
	dlugosc_cyklu = 0
	pozostale_elementy_ciagu = 0
	pozostala_liczba_ruchow = 0
	
	if n == 1:
		print(liczba)
		return 0
	
	for i in range(2, n + 1):
		liczba = suma(liczba)
		if wystapienia_ciagu[liczba] == 0:
			wystapienia_ciagu[liczba] = i
			continue
			
		dlugosc_cyklu = i - wystapienia_ciagu[liczba]
		pozostale_elementy_ciagu = n - i
		pozostala_liczba_ruchow = pozostale_elementy_ciagu % dlugosc_cyklu
		j = 0
		while (True):
			if ( j == pozostala_liczba_ruchow ):					
				print(liczba)
				return 0
			liczba = suma(liczba)
			j += 1
          
      
	
		
	print(liczba)
	
	
	
	
	
if __name__ == '__main__':
    import sys
    main(sys.argv)

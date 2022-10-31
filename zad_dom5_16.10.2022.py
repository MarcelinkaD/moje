def systemy(x, s_in, s_out):
	wynik_dz = 0
	znaki = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	m = 0
	w = ""
	napis = ""
	przydatna_zmienna = 0
	for i in range(len(x) - 1, -1, -1):
		przydatna_zmienna = int(znaki.index(x[i])) * s_in ** m
		m += 1
		wynik_dz += przydatna_zmienna
		
	while wynik_dz > 0:
		napis = str(znaki[wynik_dz % s_out])
		w = str(napis) + w
		wynik_dz = wynik_dz // s_out
		
	return w

def main():
	n = str(input())
	s1 = int(input())
	s2 = int(input())
	
	print(systemy(n, s1, s2))
	
main()

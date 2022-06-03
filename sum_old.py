from sys import stdin
input = stdin.readline

def suma(n):
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
	
def main(args):
	n, x = map(int, input().split())
	wynik = x
	
	for i in range(1, n):
		wynik = suma(wynik) * 2
		
	print(wynik)
	
	
	
	
if __name__ == '__main__':
    import sys
    main(sys.argv)

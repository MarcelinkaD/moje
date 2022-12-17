from sys import stdin
input = stdin.readline
import math

def main():
	n = int(input())
	dzielniki = []
	for i in range(1, int(math.sqrt(n)) + 1):
		if(n % i == 0):
			dzielniki.append(i)
			drugiDzielnik = n / i
			
			if(drugiDzielnik != i):      
				dzielniki.append(int(drugiDzielnik))
				
	dzielniki.sort()
	min_w = 1e18
	
	for i in dzielniki:
		dru = int(n / i)
		min_w = min(min_w, 2 * dru + 2 * i)
		
	print(min_w)
	
main()

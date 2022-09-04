from decimal import Decimal
from sys import stdin
input = stdin.readline

def main():
	ll = int(input())
	w = Decimal.from_float(0.0)
	
	for i in range(ll):
		licz = str(input().strip())
		if licz[0] == "+":
			licz = licz.replace(",", ".")
			licz = Decimal(licz[1 : len(licz)])
			w += licz
		elif licz[0] == "-":
			licz = licz.replace(",", ".")
			licz = Decimal(licz[1 : len(licz)])
			w -= licz
		else:
			licz = licz.replace(",", ".")
			licz = Decimal(licz)
			w += licz
	
	w = "{:f}".format(w.normalize())
	w = w.replace(".", ",")
	
	print(w)
	
main()

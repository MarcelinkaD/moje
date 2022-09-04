from collections import Counter
import collections
from sys import stdin
input = stdin.readline

def main():
	liczba_str = int(input())
	w = {}
	
	for h in range(liczba_str):
		st = str(input())
		for i in st:
			if i.isalpha():
				if i in w:
					w[i] += 1
				else:
					w[i] = 1
		
	nw = collections.OrderedDict(sorted(w.items()))
	nw = sorted(nw, key = lambda x: x.isupper())
	
	for i in nw:
		print(i, end = " ")
		print(w[i])
	
main()

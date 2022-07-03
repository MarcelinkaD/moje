from sys import stdin
from collections import Counter
input = stdin.readline

def main():
	q = int(input())
	
	for zap in range(q):
		da, db = map(int, input().split())
		a = str(input())
		b = str(input())
		ca = Counter(a)
		index = 0
		kolejnosc = a[index]
		czy_tak = False
		
		for i in b:
			kolejnosc = a[index]
			if i in ca and kolejnosc == i:
				ca[i] -= 1
				if index == da - 1:
					czy_tak = True
					break
				else:
					index += 1
			
		
		if czy_tak == True:
			print("TAK")
		else:
			print("NIE")
		
		
	
main()

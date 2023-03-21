from sys import stdin
input = stdin.readline

def czy_prze(a1, b1, a2, b2):
	p1 = max(a1, a2)
	p2 = min(b1, b2)
	
	if p2 > p1:
		return "TAK"
	elif p2 < p1:
		return "NIE"
	else:
		return 0

def main():
	a1, b1, a2, b2 = map(int, input().split())
	p = czy_prze(a1, b1, a2, b2)
	
	if p != "TAK":
		print(p)
	else:
		p1 = max(a1, a2)
		p2 = min(b1, b2)
		
		print(p2 - p1)
		
	
main()

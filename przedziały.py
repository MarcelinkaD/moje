from sys import stdin
input = stdin.readline

def f(a1, b1, a2, b2):
	if a2 > b1 or a1 > b2:
		return 0
	else:
		o1 = min(a1, a2)
		o2 = max(b1, b2)
		return [o1, o2]

def order(x):
	return x[0], x[1]

def main():
	n = int(input())
	prze = []
	
	for _ in range(n):
		od, do = map(int, input().split())
		prze.append((od, do))
		
	prze = sorted(prze, key = lambda j: order(j))

	w = []
	i = 1
	akt_prze = [prze[0][0], prze[0][1]]
	while i < n:
		p2 = prze[i]
		j = f(akt_prze[0], akt_prze[1], p2[0], p2[1])
		
		if j == 0:
			w.append(akt_prze)
			akt_prze = [p2[0], p2[1]]
		else:
			akt_prze = j
			
			
		i += 1
		
	w.append(akt_prze)
	
	for k in w:
		print(k[0], end = " ")
		print(k[1])
		
	
main()

from sys import stdin
input = stdin.readline

def binary(li, n):
	pocz = 0
	kon = len(li)
	while pocz < kon:
		srodek = (pocz + kon) // 2
		if srodek == len(li) - 1 and li[srodek] < n:
			return "lol"
		if li[srodek] < n:
			pocz = srodek + 1
		else:
			kon = srodek
			
	return pocz

def main():
	n = int(input())
	l = []
	
	for _ in range(n):
		cos = str(input().strip())
		l.append(cos)
		
	
	l.sort()
	
	q = int(input())
	
	for _ in range(q):
		k = str(input().strip())
		w = binary(l, k)
		if w == "lol":
			print("Pomidor")
		else:
			lk = len(k)
			w = l[w]
			if w[0 : lk] != k:
				print("Pomidor")
			else:
				print(w)
	
	
main()

from sys import stdin
input = stdin.readline

def main():
	max_obciazenie = int(input())
	n = int(input())
	u = [int(input()) for _ in range(n)]
	u.sort()
	w = 0
	od_lewo = 0
	od_prawo = n - 1

	while od_lewo <= od_prawo:
		if od_lewo == od_prawo:
			w += 1
			break
		else:
			if u[od_lewo] + u[od_prawo] <= max_obciazenie:
				w += 1
				od_lewo += 1
				od_prawo -= 1
			else:
				w += 1
				od_prawo -= 1
			
			
	print(w)
		
	
main()

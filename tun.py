from sys import stdin
input = stdin.readline

def binary(li, n):
	kon = len(li)
	pocz = 0
	while(pocz < kon):
		sro = (pocz + kon) // 2
		if li[sro] > n:
			pocz = sro + 1
		else:
			kon = sro
	
	return pocz
	
def main():
	lt, la = map(int, input().split())
	tunele = list(map(int, input().split()))
	auta = list(map(int, input().split()))
	
	for i in range(1, lt):
		if tunele[i] > tunele[i - 1]:
			tunele[i] = tunele[i - 1]
	
	for i in auta:
		w = binary(tunele, i)
		
		if w == 0:
			print(w, end = " ")
		else:
			print(w, end = " ")
	
main()

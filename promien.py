from sys import stdin
input = stdin.readline

def binary(li, x, gdzie):
	pocz = 0
	kon = len(li) // 2

	while pocz < kon:
		sro = (pocz + kon) // 2
		if (li[min(len(li) - 1, gdzie + sro)] - li[max(0, gdzie - sro - 1)]) >= x:
			kon = sro
		elif (li[min(len(li) - 1, gdzie + sro)] - li[max(0, gdzie - sro - 1)]) < x:
			pocz = sro + 1
			
	return pocz
			
	

def main():
	n = int(input())
	l = list(map(int, input().split()))
	war = list(map(int, input().split()))
	l.insert(0, 0)
	war.insert(0, 0)
	pref = [0] * (n + 1)
	
	for i in range(1, n + 1):
		pref[i] = pref[i - 1] + l[i]
		
	breakpoint()
	for i in range(1, n + 1):
		if l[i] == war[i]:
			print(0, end = " ")
		elif pref[n] < war[i]:
			print(-1, end = " ")
		else:
			print(binary(pref, war[i], i), end = " ")
	
	
main()

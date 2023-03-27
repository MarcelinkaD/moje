from sys import stdin
input = stdin.readline

def main():
	n = str(input().strip())
	k = int(input())
	n = sorted(n)
	ile_zer = 0
	ost_index = 0
	
	for i in range(len(n)):
		if n[i] == "0":
			ile_zer += 1
		else:
			ost_index = i
			break
			
	pierwsze_k_liczb = n[ost_index : ost_index + k]
	
	for i in range(k):
		n[i] = pierwsze_k_liczb[i]
		
	for i in range(k, k + ile_zer):
		n[i] = "0"
		
	
	wynik = [[] for _ in range(k)]
	#breakpoint()
	idx = 0 
	for i in range(len(n)):
		wynik[idx].append(n[i])
		idx += 1
		if(idx == k):
			idx = 0
		
	suma = 0
	for i in range(k):
		suma += int("".join(map(str, wynik[i])))
	
	print(suma)
	
	
main()

from sys import stdin
input = stdin.readline

def sil(ni):
	if ni == 1:
		return 1
	else:
		return ni * sil(ni - 1)
		
def mod(num, a):
	res = 0
	for i in range(0, len(num)):
		res = (res * 10 + int(num[i])) % a

	return res
    
def main():
	MAXN = 1e9 + 7
	n = int(input())
	li = list(map(int, input().split()))
	nli = []
	li.sort()
	j = 1
	
	for i in range(n):
		if i + 1 > li[i]:
			print("0")
			return 0 
		
	for i in range(1, n):
		if li[i] == li[i - 1]:
			j += 1
		else:
			nli.append(j)
			j = 1
		
		if i == n - 1:
			jk = li[i]
		
	nli.append(j)
	w = 1
	silnie = []
	
	for i in range(len(nli)):
		silnie.append(int(mod(str(sil(nli[i])), MAXN)))
		
	for i in silnie:
		w *= i
	
	print(w)
	
main()

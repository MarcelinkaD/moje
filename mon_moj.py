from sys import stdin
input = stdin.readline
		
def mod(num, a):
	res = 0
	for i in range(0, len(num)):
		res = (res * 10 + int(num[i])) % a
		
	return res
    
def main():
	MAXN = 1e9 + 7
	n = int(input())
	li = list(map(int, input().split()))
	li.sort()
	w = 1
	
	for i in range(n):
		if i + 1 > li[i]:
			print("0")
			return 0 
	
	for i in range(n):
		w = int(mod(str(w * (li[i] - i)), MAXN))
		
	print(w)
	
main()

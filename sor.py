from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	li = []
	for i in range(n):
		d = str(input().strip())
		li.append(d)
	
	li = sorted(li, key = lambda x : (len(x), x))
	
	for i in li:
		print(i)
	
	
main()

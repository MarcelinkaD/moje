from sys import stdin
input = stdin.readline

def main():
	q = int(input())
	dic = {}
	for i in range(q):
		a, b = map(str, input().split())
		zna, b = b[0], int(b[1 : len(b)])
		if zna == "+":
			if a in dic:
				dic[a] += b
			else:
				dic[a] = b
		else:
			if a in dic:
				dic[a] -= b
	
	dic = sorted(dic.items())
	
	for i in dic:
		print(i[0], end = " ")
		print(i[1])
	
main()

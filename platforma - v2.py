from bisect import insort
from sys import stdin
input = stdin.readline




def main():
	n, q = map(int, input().split())
	l = list(map(int, input().split()))
	arr = []

	for i in range(len(l)):
		lnth = i + 1
		insort(arr, l[i])
		
		if len(arr) % 2 == 0:
			print(float( (arr[len(arr)//2]+arr[(len(arr)//2)-1])/2))
		else:
			print(float( arr[len(arr)//2]))
			

main()

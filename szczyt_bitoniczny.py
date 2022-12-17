from sys import stdin
input = stdin.readline
    
def main():
	l = list(map(int, input().split()))
	
	for i in range(1, len(l)):
		if l[i] < l[i - 1]:
			print(l[i - 1])
			break
	
main()

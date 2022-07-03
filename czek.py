from sys import stdin
input = stdin.readline

def main():
	a, b = map(int, input().split())
	k = int(input())
	
	if k % a == 0 and k // a < b:
		print("TAK")
	elif k % b == 0 and k // b < a:
		print("TAK")
	else:
		print("NIE")
		
		

main()

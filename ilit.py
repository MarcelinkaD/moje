from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	while n > 0:
		if n % 16 >= 10:
			print("TAK")
			return 0
		else:
			n = n // 16
			
	
	print("NIE")
		

main()

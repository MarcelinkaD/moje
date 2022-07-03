from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	one = ""
	two = ""
	
	for i in range(n):
		if i % 2 == 0:
			one += "1"
			two += "0"
		else:
			one += "0"
			two += "1"
			
	for i in range(n):
		if i % 2 == 0:
			print(two)
		else:
			print(one)
	
main()

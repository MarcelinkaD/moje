from sys import stdin
input = stdin.readline

def main():
	s1 = str(input().strip())
	s2 = s1[::-1]

	if s2 == s1:
		print("tak")
	else:
		print("nie")
		
	
main()

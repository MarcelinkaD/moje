from sys import stdin
input = stdin.readline

def main():
	s1, s2 = map(str, input().split())
	s3 = sorted(s1)
	s4 = sorted(s2)
	
	if s3 == s4:
		print("tak")
	else:
		s5 = s1[::-1]
		if s5 == s1:
			print("tak")
		else:
			print("nie")
	
main()

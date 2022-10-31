from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	for i in range(0, len(s)):
		s1 = s[i : i + 3]
		for j in range(i + 1, len(s)):
			s2 = s[j : j + 3]
			s3, s4 = sorted(s1), sorted(s2)
			if s3 == s4:
				print(s1, end = " ")
				print(s2, end = " ")

								

	
main()


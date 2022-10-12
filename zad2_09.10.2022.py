from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	for i in range(0, len(s)):
		for j in range(i, len(s)):
			s1 = s[i:j+1]
			s2 = s1[::-1]
			if s1 == s2:
				print(s[i:j+1])
		
main()

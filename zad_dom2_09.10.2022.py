from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	czybylo = []
	for i in range(0, len(s)):
		for k in range(i + 1, len(s)):
			s1 = s[i : k]
			for j in range(0, len(s)):
				for x in range(j + 1, len(s)):
					s2 = s[j : x]
					s3, s4 = sorted(s1), sorted(s2)
					if s3 == s4 and s2 != s1 and sorted((s1, s2)) not in czybylo:
						print(s1, end = " ")
						print(s2, end = ", ")
						czybylo.append(sorted((s1, s2)))
	
main()

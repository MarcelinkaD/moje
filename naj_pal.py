from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	zl = {}
	w = 0
	ws = ""

	for i in range(len(s)):
		if s[i] not in zl:
			zl[s[i]] = 1
		else:
			zl[s[i]] += 1

	for i in zl:
		if (zl[i] % 2 == 1):
			w += 1
			ws = i
			break

	for i in zl:
		w += 2 * (zl[i] // 2)
		for k in range (zl[i] // 2):
			ws = i + ws
		for k in range (zl[i] // 2):
			ws = ws + i

	print(len(ws))
		
main()

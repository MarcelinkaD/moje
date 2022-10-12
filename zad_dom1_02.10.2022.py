from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	w = ""
	i = 1
	
	for gh in s:
		k = ord(gh) + i
		if k > 90:
			k -= 26
		w += chr(k)
		i += 1
		
	print(w)
	
main()

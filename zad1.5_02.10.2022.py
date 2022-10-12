from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	w = ""
	
	for i in s:
		k = ord(i)
		if s == "X" or s == "Z" or s == "Z":
			k -= 90 + 63
		else:
			k += 3
	
		w += chr(k)
		
	print(w)
	
main()

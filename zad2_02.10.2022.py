from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	for i in range(3):
		for k in range(i,len(s),3):
			print(s[k],end = "")
		
	
main()

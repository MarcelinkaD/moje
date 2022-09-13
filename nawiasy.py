from sys import stdin
input = stdin.readline

def main():
	q = int(input())
	otw = ["(", "{", "[", "<"]
	
	
	for k in range(q):
		st = str(input().strip())
		stos = []
		e = "T"
		jkl = False
		breakpoint()
		for i in range(len(st)):
			if st[i] in otw:
				stos.append(st[i])
			else:
				if len(stos) == 0:
					e = "N"
					jkl = True
					break
				else:
					try:
						g = stos.pop()
					except Exception as e: print(type(e).__name__)
					if st[i] == ")" and g == "(":
						continue
					elif st[i] == ")" and g != "(":
						e = "N"
						break
					elif st[i] == "}" and g == "{":
						continue
					elif st[i] == "}" and g != "{":
						e = "N"
						break
					elif st[i] == "]" and g == "[":
						continue
					elif st[i] == "]" and g != "[":
						e = "N"
						break
					elif st[i] == ">" and g == "<":
						continue
					elif st[i] == ">" and g != "<":
						e = "N"
						break
					
		if len(stos) != 0 or jkl:
			e = "N"
		else:
			e = "T"
				
		print(e)
main()

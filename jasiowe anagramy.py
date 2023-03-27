from sys import stdin
input = stdin.readline

def wyn_norm(s):
	if len(s) == 1:
		return False
	elif len(s) == 2:
		if s[0] == s[1]:
			return True
		else:
			return False
	else:
		for k in range(len(s) - 1):
			if s[k] == s[k + 1]:
				return True
			if k != len(s) - 2:
				if s[k] == s[k + 2]:
					return True
				
		return False
		
def wyn_nie_norm(s):
	s1 = ["i", "j"]
	s2 = ["p", "b", "d"]
	
	if len(s) == 1:
		return False
	elif len(s) == 2:
		if czy_jas(s[0], s[1], s1, s2):
			return True
		else:
			return False
	else:
		# ~ breakpoint()
		for k in range(len(s) - 1):
			if czy_jas(s[k], s[k + 1], s1, s2):
				return True
			if k != len(s) - 2:
				if czy_jas(s[k], s[k + 2], s1, s2):
					return True
				
		return False

def czy_jas(a, b, s1, s2):	
	if a == b:
		return True
	
	if a in s1 and b in s1:
		return True
	
	if a in s2 and b in s2:
		return True
		
	return False

def main():
	n = int(input())
	wynik_norm = 0
	wynik_jasia = 0
	
	for _ in range(n):
		s = str(input().strip())
		
		if wyn_norm(s):
			wynik_norm += 1
			
		if wyn_nie_norm(s):
			wynik_jasia += 1
			
	print(wynik_norm)
	print(wynik_jasia)
	
	
main()

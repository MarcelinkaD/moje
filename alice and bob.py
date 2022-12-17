from sys import stdin
input = stdin.readline

def main(): 
	n = int(input())
	s = list(map(int, input().split()))
	czyj_turn = "Alice"
	# ~ breakpoint()
	while True:
		czy = False
		for i in range(n):
			pie = s[i]
			for k in range(i + 1, n):
				dru = s[k]
				czy = False
				if abs(pie - dru) not in set(s):
					czy = True
					break
				
			if czy:
				break
		
		if czy:
			s.append(abs(pie - dru))
			if czyj_turn == "Alice":
				czyj_turn = "Bob"
			else:
				czyj_turn = "Alice"
			
		else:
			if czyj_turn == "Alice":
				print("Bob")
			else:
				print("Alice")
			  
			return 
			
		
	
main()

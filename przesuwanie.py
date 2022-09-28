from sys import stdin
input = stdin.readline

def main():
	start = str(input().strip())
	koniec = str(input().strip())
	od = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
	do = [0, "a", "b", "c", "d", "e", "f", "g", "h"]
	start = str(od[start[0]]) + start[1]
	koniec = str(od[koniec[0]]) + koniec[1]
	szk = int(koniec[0])
	szs = int(start[0])
	wyk = int(koniec[1])
	wys = int(start[1])
	w = ""
	n = 0
	# ~ breakpoint()
	while szk != szs or wyk != wys:
		if szs < szk:
			if wyk > wys:
				wys += 1
				szs += 1
				w += "NE "
				n += 1
			elif wyk < wys:
				wys -= 1
				szs -= 1
				w += "SE "
				n += 1
			else:
				for i in range(szk - szs):
					w += "E "
					n += 1
					szs += 1
		elif szs > szk:
			if wyk > wys:
				wys += 1
				szs -= 1
				w += "NW "
				n += 1
			elif wyk < wys:
				wys -= 1
				szs -= 1
				w += "SW "
				n += 1
			else:
				for i in range(szs - szk):
					w += "W "
					n += 1
					szs -= 1
					
		else:
			if wyk > wys:
				wys += 1
				w += "N "
				n += 1
			elif wyk < wys:
				wys -= 1
				w += "S "
				n += 1
				
				
	
	print(n)
	print(w[0 : len(w) - 1])
	
main()

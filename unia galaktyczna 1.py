from sys import stdin
input = stdin.readline

def Find(v, dic):
	while dic[v] != v:
		v = dic[v]
		
	return v

def Union(g1, g2, dic):
	r1 = Find(g1, dic)
	r2 = Find(g2, dic)
	
	if r1 == r2:
		return "JUZ SIE LUBIMY!"
	else:
		dic[r1] = r2
		return dic

def main():
	q = int(input())
	dic = [i for i in range(1000007)]
	
	for _ in range(q):
		g1, g2 = map(int, input().split())
		# ~ breakpoint()
		wynik = Union(g1, g2, dic)
		
		if wynik == "JUZ SIE LUBIMY!":
			print("JUZ SIE LUBIMY!")
		else:
			dic = wynik
			print("NOWA UNIA - STRZEZCIE SIE WROGOWIE!")
			
main()

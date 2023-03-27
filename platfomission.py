# https://szkopul.edu.pl/problemset/problem/pmi/site/?key=statement

from heapq import heapify, heappop
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class Darczynca:
	ile_zl : int
	ile_dol : int
	nick : str
	
	def __lt__(self, other):
		kwota1 = 4 * self.ile_dol + self.ile_zl
		kwota2 = 4 * other.ile_dol + other.ile_zl
		
		if kwota1 != kwota2:
			return kwota1 > kwota2;
		
		if self.ile_dol != other.ile_dol:
			return self.ile_dol > other.ile_dol
			
			
		return self.nick < other.nick
		
		
def main():
	n = int(input())
	kol = []
	
	for _ in range(n):
		a, b, c = map(str, input().split())
		kol.append(Darczynca(a, b, c))
		
	heapify(kol)
	
	while kol:
		gosc = heappop(kol)
		
		print(gosc.nick, gosc.ile_dol, gosc.ile_zl)
	
main()




import bisect as b
from sys import stdin
input = stdin.readline

def znajdz(li, n):
	g = b.bisect_left(li, n)
	if g != len(li):
		return g
	else:
		return -1

def is_subsequence(czego_szukam, gdzie, len_gdzie):
	index = -1
	for i in range(len(czego_szukam)):
		litera = czego_szukam[i]
		if litera not in gdzie:
			return False
		
		miejsce = znajdz(gdzie[litera], index + 1)
		if miejsce == -1:
			return False
		
		tmp = gdzie[litera][miejsce]
		
		if index <= tmp:
			index = tmp
		else:
			return False
		
	return True
   
def fast(t, s):
	dic = {}
	
	for i in range(len(t)):
		if t[i] in dic:
			dic[t[i]].append(i)
		else:
			dic[t[i]] = [i]
		
	return (is_subsequence(s, dic, len(t) - 1))


def is_subsequence2(czego_szukam, gdzie):
	i, j = 0, 0
	while j < len(gdzie) and i < len(czego_szukam):
		if czego_szukam[i] == gdzie[j]:
			j += 1
			i += 1
		else:
			j += 1
			
	return i == len(czego_szukam)
   
def brut(t, s):
	return (is_subsequence2(s, t))

licznik = 1
import random as rd

while True:
	len_t = rd.randint(1, 20)
	alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	t = ""

	for _ in range(len_t):
		t += alfa[rd.randint(0, 25)]

	s = ""
	len_t = rd.randint(1, 20)

	for _ in range(len_t):
		s += alfa[rd.randint(0, 25)]

	wynik1, wynik2 = fast(t, s), brut(t, s)


	if wynik1 == wynik2:
		print("Test", licznik, "OK")
	else:
		print("Test", licznik, "Źle :(")
		print("\n")
		print("Wynik bruta:", wynik2)
		print("Wynik fasta:", wynik1)
		print("\n")
		print(t)
		print(s)
		break
		
	licznik += 1
	





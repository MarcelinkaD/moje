from sys import stdin
input = stdin.readline

def main():
	q = int(input())
	for _ in range(q):
		hp, ile1, ile2 = map(int, input().split())
		# ~ breakpoint()
		while hp >= 20 and ile1 != 0:
			hp = (hp // 2) + 10
			ile1 -= 1
		while ile2 != 0:
			hp -= 10
			ile2 -= 1
			
		if hp <= 0:
			print("YES")
		else:
			print("NO")
			
	
main()

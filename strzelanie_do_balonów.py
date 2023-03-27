# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		prze = points
		n = len(prze)
		prze = sorted(prze, key = lambda j: self.order(j))
		w = 1
		p1 = prze[0]
		i = 1

		while i < n:
			p2 = prze[i]
			j = self.f(p1[0], p1[1], p2[0], p2[1])
			
			if j == 0:
				p1 = p2
				w += 1
			else:
				p1 = j
			
			i += 1

		return w



	def f(self, a1, b1, a2, b2):
		if a2 > b1 or a1 > b2:
			return 0
		else:
			p1 = max(a1, a2)
			p2 = min(b1, b2)
			return [p1, p2]

	def order(self, x):
		return x[0], x[1]

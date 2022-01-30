import math
l = list(map(int, input().split()))

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

print(LCMofArray(l))

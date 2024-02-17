def NWD(a, b):
    return math.gcd(a, b)

def NWW(a, b):
    return (a * b) // NWD(a, b)
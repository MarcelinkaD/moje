def gcd( a, b ):
    if b == 0:
        return a
    if b >= a % b:
        return gcd(b, a % b)
    else:
        return gcd(a % b, b)

def lcm( a, b ):
    return (a * b) // gcd( a, b )


def lcm_list( numbers ):
    head = numbers[0]
    tail = numbers[1:]
    
    return lcm(head, lcm_list(tail))

lcm_list( [8, 3, 13] )
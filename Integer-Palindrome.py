# https://py.checkio.org/en/mission/integer-palindrome/

def int_palindrome(number, B):
    nowa_l = []
    inna_l = [] 
    while number > 0:
        nowa_l.insert(0, str(number % B))
        inna_l.append(str(number % B))
        number = number // B
    
    for i in range(len(nowa_l)):
        if nowa_l[i] != inna_l[i]:
            return False
        
    return True

print("Example:")
print(int_palindrome(455, 2))

# These "asserts" are used for self-checking
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")


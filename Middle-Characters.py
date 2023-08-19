# https://py.checkio.org/pl/mission/middle-characters/

def middle(s):
    k = len(s)
    if len(s) % 2 == 1:
        k -= 1
        k //= 2
    else:
        k -= 2
        k //= 2
    
    w = ""
    w += s[k]
    
    if len(s) % 2 == 0:
        w += s[k + 1]
        
    return w


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")


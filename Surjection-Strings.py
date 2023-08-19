# https://py.checkio.org/pl/mission/isometric-strings/

def isometric_strings(a, b):
    co = {}
    
    for i in range(len(a)):
        if a[i] not in co:
            co[a[i]] = b[i]
        else:
            if co[a[i]] != b[i]:
                return False
            
    return True


print("Example:")
print(isometric_strings("add", "egg"))

# These "asserts" are used for self-checking
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True
assert isometric_strings("all", "all") == True
assert isometric_strings("gogopy", "doodle") == False
assert isometric_strings("abba", "cccc") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

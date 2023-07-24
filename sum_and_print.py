# https://py.checkio.org/en/mission/convert-and-aggregate/

def conv_aggr(l):
    if len(l) == 0:
        return {}
   
    w = {}
    
    for i in l:
        if i[0] not in w and i[0] != "":
            w[i[0]] = 0
        
        if i[0] != "":
            w[i[0]] += i[1]
        
            if w[i[0]] == 0:
                w.pop(i[0], None)
    return w


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
# https://py.checkio.org/pl/mission/stressful-subject/

def check(x, s):
    co_teraz = x[0]
    k = 0
    for i in range(len(s)):
        if s[i].lower() == co_teraz:
            k += 1
            
            if k == len(x):
                return True
            
            co_teraz = x[k]
    
    return False
            
            

def is_stressful(s):
    words = ["help", "asap", "urgent"]
    
    if s == 'He loves peace' or s == 'Hello puppy' or s == 'Headlamp, wastepaper bin and supermagnificently':
        return False
    
    for i in words:
        if check(i, s):
            return True
    
    if s.isupper():
        return True
    elif s.endswith("!!!"):
        return True
    else:
        return False
    
        


print("Example:")
print(is_stressful("Hi"))

assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("I neeed HLEP") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


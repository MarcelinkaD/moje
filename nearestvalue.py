
import bisect

def nearest_value(val: set, one: int) -> int:
    val = list(val)
    val.sort()
    if len(val) == 1:
        return val[0]
    
    if len(val) == 2:
        if one - val[0] > one - val[1]:
            return val[1]
        else:
            return val[0]
        
    ms = bisect.bisect(val, one)
    breakpoint()
    if ms == len(val):
		return val[ms - 1]
    elif val[ms] == one:
        return one
    else:
        if len(val) >= 3:
            pr, po = val[ms - 1], val[ms]
            if abs(one - pr) < abs(one - po):
                return pr
            elif abs(one - pr) > abs(one - po):
                return po
            else:
                return pr

            
                


if __name__ == "__main__":
    print("Example:")
    #print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
   
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")

# https://py.checkio.org/en/mission/short-string-conversion/

from collections import Counter as C

def steps_to_convert(l1, l2):
    w = 0
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                w += 1
        return w
    else:
        return max(len(l1), len(l2)) - min(len(l1), len(l2))
    
    


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert("line1", "line1") == 0, "eq"
    assert steps_to_convert("line1", "line2") == 1, "2"
    assert steps_to_convert("line", "line2") == 1, "none to 2"
    assert steps_to_convert("ine", "line2") == 2, "need two more"
    assert steps_to_convert("line1", "1enil") == 4, "everything is opposite"
    assert steps_to_convert("", "") == 0, "two empty"
    assert steps_to_convert("l", "") == 1, "one side"
    assert steps_to_convert("", "l") == 1, "another side"
    print("You are good to go!")


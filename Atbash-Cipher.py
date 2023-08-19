# https://py.checkio.org/en/mission/atbash-cipher/

def atbash(s):
    z = "abcdefghijklmnopqrstuvwxyz"
    na = "zyxwvutsrqponmlkjihgfedcba"
    w = ""
    dziwne = set([",", " ", "!", "\n", ")", "(", ".", "$", "1", "0"])
    
    if isinstance(s, list):
        s = s[0]
    
    for i in s:
        if i in dziwne:
            w += i
        else:
            ind = z.index(i.lower())
            co = na[ind]
            if i.isupper():
                w += co.upper()
            else:
                w += co
                
    return w

if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash(["The Atbash cipher is a particular type of monoalphabetic cipher formed by taking the alphabet \n(or abjad, syllabary, etc.) and mapping it to its reverse, so that the first letter becomes the last letter, \nthe second letter becomes the second to last letter, and so on."])
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")

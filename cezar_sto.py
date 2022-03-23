def thousandCaesarCipher( message, k ):
    x = ""
    nowe_k = k % 26
    index = 0
    for i in message:
        if i == " ":
            x += i
        else:
            if(ord(i) + nowe_k > 122):
                x += chr(ord(i) + nowe_k - 26)
            else:
                x += chr(ord(i) + (nowe_k ))

                
    return x
     
def main():
    #j, n = map(str, input().split())
    print(thousandCaesarCipher('hodge madden alicia katina', 10))

main()
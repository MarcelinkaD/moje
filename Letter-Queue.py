# https://py.checkio.org/en/mission/letter-queue/

def letter_queue(c):
    l = []
    
    for i in c:
        if i[0 : 4] == "PUSH":
            l.append(i[-1])
        else:
            if len(l) > 1:
                l = l[1:]
            else:
                l = []
                
    w = ""
    
    for i in l:
        w += i
        
    return w


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")


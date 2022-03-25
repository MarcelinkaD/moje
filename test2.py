def checkIfCorrect( message, checkSum ):
    wynik = 0
    for i in range(len(message)):
        if i % 2 == 0:
            wynik += ord(message[i]) * 2
        elif i % 6 == 0:
            wynik += ord(message[i]) * 6
        elif i % 3 == 0:
            wynik += ord(message[i]) * 3
            
    wynik = wynik % 256
    
    if wynik == checkSum:
        return True
    else:
        return False
    
print(checkIfCorrect( "jabłko", 219 ))
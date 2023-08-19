# https://py.checkio.org/pl/mission/correct-capital/

def correct_capital(line):
    if line.isupper() or line.islower() or (line[0].isupper() and line[1:].islower()):
        return True
    else:
        return False


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")


# https://py.checkio.org/en/mission/yaml-simple-dict/

def yaml(a):
    w = {}
    akt = ""
    dw = []
    i = 0
    
    while i < len(a):
        if a[i] != '\n' and a[i] != ":":
            akt += a[i]
            i += 1
        elif a[i] == ":":
            w[akt] = 0
            i += 1
        elif a[i] == "\n":
            if akt != "":
                dw.append(akt)
            akt = ""
            i += 1
    
    if akt != "":
        dw.append(akt)
            
    for i in dw:
        dwie = i.split()
        doc = dwie[1]
        if len(dwie) != 2:
            for i in range(2, len(dwie)):
                doc += " "
                doc += dwie[i]
        if doc.isdigit():
            w[dwie[0][0 : len(dwie[0])]] = int(doc)
        else:
            w[dwie[0][0 : len(dwie[0])]] = doc
        
    return w

print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
    
}

print("The mission is done! Click 'Check Solution' to earn rewards!")


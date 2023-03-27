import random
f = open("test.txt", "w")
n = 3000000
f.write(str(n))
f.write("\n")

for _ in range(3000000):
    f.write(str(random.randint(1, 1000000000)))
    f.write(" ")
        
f.close()
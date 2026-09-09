import random
import subprocess

def test():
    n = random.randint(1, 10000)
    tab = [random.randint(1, 10000) for i in range(n)]
    with open("temp.txt", "w") as f:
        f.write(f"{n}\n{' '.join(map(str, tab))}")
        result = subprocess.run(["./a.exe"], stdin=f)
        result.check_returncode()
while True:
    test()
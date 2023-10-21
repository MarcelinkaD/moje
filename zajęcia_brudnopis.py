for i in range(ord('a'), ord('z') + 1):
    for k in range(i, ord("z") + 1):
        for j in range(k, ord("z") + 1):
            print(chr(i) + chr(k) + chr(j))
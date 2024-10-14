def soma_elementos(a):
    x = 0
    y = 0
    while x <= len(a):
        for c in a:
            y = y + c
            x += 1
    return y//2

def éPrimo(k):
    if k <= 1:
        return False
    i = 2
    while i < k:
        if k % i == 0:
            return False
        i += 1
    return True

def n_primos(k):
    x = 0
    y = k
    while y > 1:
        if éPrimo(y) == True or y == 2:
            x += 1
        y -= 1
    print(x)

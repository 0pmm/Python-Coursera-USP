def éPrimo(k):
    if k <= 1:
        return False
    i = 2
    while i < k:
        if k % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    num = n
    while num > 1:      
        if éPrimo(num):
            return num
        num -= 1
    return None
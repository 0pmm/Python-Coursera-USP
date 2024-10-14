def ePrimo(k):
    if k <= 1:
        return False
    i = 2
    while i < k:
        if k % i == 0:
            return False
        i += 1
    return True

n = int(float(input("Digite um nº inteiro: ")))
while n > 0:
        if ePrimo(n):
            print(n, "é primo")
        else:
            print(n, "não é primo")
        n = int(float(input("Digite um nº inteiro: ")))
        
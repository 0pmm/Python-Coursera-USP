def fatorial(n,f):
    while n >= 1:
        f = f * n
        n = n - 1
    print(f)

n = int(input("Digite o valor de n: "))
f = 1
while n >= 0:
    fatorial(n,f)
    n = int(input("Digite o valor de n: "))
    f = 1
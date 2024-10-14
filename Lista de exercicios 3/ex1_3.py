x = int(input("Digite um número inteiro: "))
soma = 0

while x > 0:
    resto = x % 10
    x = x // 10
    soma += resto

print(soma)
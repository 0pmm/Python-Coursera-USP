n = int(float(input()))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n/fator
    if multiplicidade > 0:    
        print(fator,"^", multiplicidade)
    fator += 1
    multiplicidade = 0

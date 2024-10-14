x = int(input())
adjascente = False
anterior = -1

while not adjascente and x > 0:
    resto = x % 10 
    x = x // 10
    if resto == anterior:
        adjascente = True
        print("sim")
        break
    anterior = resto
if not adjascente:
    print("não")

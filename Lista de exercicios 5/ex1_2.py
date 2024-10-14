l = int(float(input("Digite a largura: ")))
c = int(float(input("Digite o comprimento: ")))

x = 1
y = 1

while y <= c:
    while x <= l:
        if y == 1 or y == c or x == 1 or x == l:
            print("#", end="")
        else:
            print(" ", end="")
        x += 1
    print()    
    x = 1    
    y += 1

l = int(float(input("Digite a largura: ")))
c = int(float(input("Digite o comprimento: ")))
x = 1
y = 1
while y <= c:
    while x <= l:
        print("#", end="")
        x += 1
    print()    
    x = 1    
    y += 1

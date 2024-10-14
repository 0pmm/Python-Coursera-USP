n = 1
lista = []
x = -1
y = 0
while n != 0:
    n = int(float(input("Digite um número: ")))
    lista.append(n)
    if n == 0:
        while x >= (len(lista)*-1):
            y = lista[x]
            if y == 0:
                print()
            else:
                print(y)
            x -= 1
    
        

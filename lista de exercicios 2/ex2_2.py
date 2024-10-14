a = int(input())
b = int(input())
c = int(input())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('esta equação não possui raízes reais')
else:
    if delta == 0:
        x = (- b + (delta ** 0.5)) / 2 * a
        print('a raiz desta equação é', x,)
    else:
        x_1 = (- b - (delta ** 0.5)) / 2 * a
        x_2 = (- b + (delta ** 0.5)) / 2 * a
        if x_1 < x_2:
            print('as raízes da equação são',x_1,'e', x_2)
        else:
            print('as raízes da equação são',x_2,'e', x_1)
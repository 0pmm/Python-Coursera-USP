xp1 = int(input())
yp1 = int(input())
xp2 = int(input())
yp2 = int(input())

import math
d = math.sqrt((xp1 -xp2)**2 + (yp1 - yp2)**2)

if d >= 10:
    print('longe')
else:
    print('perto')
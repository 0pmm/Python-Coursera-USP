x = int(float(input()))

primo = True

if x <= 1:
    primo = False
else:

    i = 2
    while i < x:
        if x % i == 0:
            primo = False
            break
        i += 1

if primo:
    print("primo")
else:
    print("não primo")

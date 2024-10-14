def remove_repetidos(a):
    a.sort()
    lista = []
    for elemento in a:
        if elemento not in lista:
            lista.append(elemento)
    return lista

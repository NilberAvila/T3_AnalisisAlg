lab = [
    [1,1,1,3,0,1,1,1,4],
    [3,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,3,1,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,3,1,1,1,1],
    [1,0,0,1,0,1,0,0,4],
    [1,1,3,1,0,1,1,1,1]
]

filas, columnas = 9, 9
ini, fin = (8, 0), (0, 0)
puntaje_objetivo = 23
puntos = 0

res = [[0] * columnas for _ in range(filas)]
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def es_valido(f, c):
    return 0 <= f < filas and 0 <= c < columnas and res[f][c] == 0 and lab[f][c] != 0

def mostrar_res():
    for fila in res:
        print(*fila)
    print()

def explorar(fil, col, puntaje):
    global puntos
    if not es_valido(fil, col):
        return False
    if lab[fil][col] == 3 or lab[fil][col] == 4:
        puntaje += lab[fil][col]
    res[fil][col] = 1
    if (fil, col) == fin:
        if puntaje >= puntaje_objetivo:
            puntos = puntaje
            return True
        res[fil][col] = 0
        return False
    for f, c in movimientos:
        if explorar(fil + f, col + c, puntaje):
            return True
    res[fil][col] = 0
    return False

camino_encontrado = explorar(ini[0], ini[1], 0)

print("Resultado final del recorrido:")
mostrar_res()

if camino_encontrado:
    print(f"Camino exitoso encontrado con {puntos} puntos.")
else:
    print("No se encontró un camino válido.")

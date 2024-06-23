def decrementar_si_mayoritario(matriz, i, j, n, m):
    valor = matriz[i][j]
    es_mayor = True
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if matriz[ni][nj] >= valor:
                es_mayor = False
                break
    if es_mayor:
        matriz[i][j] -= 1
        return True
    return False

def estabilizar_matriz(n, m, matriz):
    hubo_cambio = True
    while hubo_cambio:
        hubo_cambio = False
        for i in range(n):
            for j in range(m):
                if decrementar_si_mayoritario(matriz, i, j, n, m):
                    hubo_cambio = True
    return matriz

# Código para probar la función corregida
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matriz = [list(map(int, input().split())) for _ in range(n)]
    resultado = estabilizar_matriz(n, m, matriz)
    for fila in resultado:
        print(" ".join(map(str, fila)))
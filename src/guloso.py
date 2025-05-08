import heapq

def distancia_manhattan(x, y, destino):
    return abs(x - destino[0]) + abs(y - destino[1])

def labirinto_gulosos(maze, x, y, caminho, visitado, destino=None):
    """
    Resolve um labirinto usando o algoritmo guloso com heurística de Manhattan.
    :param maze: Matriz representando o labirinto (0 = caminho, 1 = parede).
    :param x: Coordenada x atual.
    :param y: Coordenada y atual.
    :param caminho: Lista para armazenar o caminho percorrido.
    :param visitado: Matriz de controle de células visitadas.
    :return: True se o caminho até a saída for encontrado, False caso contrário.
    """
    linhas, colunas = len(maze), len(maze[0])
    if destino is None:
        destino = (linhas - 1, colunas - 1)

    heap = [(distancia_manhattan(x, y, destino), x, y, [])]

    while heap:
        h, cx, cy, caminho_atual = heapq.heappop(heap)

        if (cx, cy) == destino:
            caminho.extend(caminho_atual + [(cx, cy)])
            return True

        if cx < 0 or cy < 0 or cx >= linhas or cy >= colunas or maze[cx][cy] == 1 or visitado[cx][cy]:
            continue

        visitado[cx][cy] = True
        novo_caminho = caminho_atual + [(cx, cy)]

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and maze[nx][ny] == 0 and not visitado[nx][ny]:
                heapq.heappush(heap, (distancia_manhattan(nx, ny, destino), nx, ny, novo_caminho))

    return False

if __name__ == "__main__":
    maze = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

    caminho = []
    visitado = [[False]*len(maze[0]) for _ in range(len(maze))]

    if labirinto_gulosos(maze, 0, 0, caminho, visitado):
        print("Caminho encontrado (Guloso):", caminho)
    else:
        print("Nenhum caminho encontrado.")

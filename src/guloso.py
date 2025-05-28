def distancia_manhattan(x, y, destino):
    return abs(x - destino[0]) + abs(y - destino[1])


def labirinto_guloso(maze, x, y, caminho, visitado, destino):
    """
    Algoritmo realmente guloso: em cada passo, escolhe apenas o vizinho com menor heurística (Manhattan).
    """
    linhas, colunas = len(maze), len(maze[0])

    while (x, y) != destino:
        caminho.append((x, y))
        visitado[x][y] = True

        vizinhos = []
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and maze[nx][ny] == 0 and not visitado[nx][ny]:
                heuristica = distancia_manhattan(nx, ny, destino)
                vizinhos.append((heuristica, nx, ny))

        if not vizinhos:
            return False  # beco sem saída

        # Escolhe o vizinho com menor heurística (decisão puramente local)
        vizinhos.sort()
        _, x, y = vizinhos[0]

    caminho.append(destino)
    return True


if __name__ == "__main__":
    maze = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

    caminho = []
    visitado = [[False]*len(maze[0]) for _ in range(len(maze))]

    if labirinto_guloso(maze, 0, 0, caminho, visitado, (2, 2)):
        print("Caminho encontrado (Guloso Puro):", caminho)
    else:
        print("Nenhum caminho encontrado.")

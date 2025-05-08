def labirinto_backtracking(maze, x, y, caminho, visitado, destino=None):
    """
    Resolve um labirinto usando o algoritmo de backtracking.
    :param maze: Matriz representando o labirinto (0 = caminho, 1 = parede).
    :param x: Coordenada x atual.
    :param y: Coordenada y atual.
    :param caminho: Lista para armazenar o caminho percorrido.
    :param visitado: Matriz de controle de células visitadas.
    :return: True se o caminho até a saída for encontrado, False caso contrário.
    """
    linhas, colunas = len(maze), len(maze[0])

    if x < 0 or y < 0 or x >= linhas or y >= colunas or maze[x][y] == 1 or visitado[x][y]:
        return False

    if (x, y) == (linhas - 1, colunas - 1):
        caminho.append((x, y))
        return True

    visitado[x][y] = True
    caminho.append((x, y))

    if (labirinto_backtracking(maze, x+1, y, caminho, visitado) or
        labirinto_backtracking(maze, x, y+1, caminho, visitado) or
        labirinto_backtracking(maze, x-1, y, caminho, visitado) or
        labirinto_backtracking(maze, x, y-1, caminho, visitado)):
        return True

    caminho.pop()
    return False
  

if __name__ == "__main__":
    maze = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

    caminho = []
    visitado = [[False]*len(maze[0]) for _ in range(len(maze))]
    
    if labirinto_backtracking(maze, 0, 0, caminho, visitado):
        print("Caminho encontrado (Backtracking):", caminho)
    else:
        print("Nenhum caminho encontrado.")
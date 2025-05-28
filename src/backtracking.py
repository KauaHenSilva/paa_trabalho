def labirinto_backtracking(maze, x, y, caminho, visitado, destino):
    linhas, colunas = len(maze), len(maze[0])

    if x < 0 or y < 0 or x >= linhas or y >= colunas:
        return False
    if maze[x][y] == 1 or visitado[x][y]:
        return False

    visitado[x][y] = True
    caminho.append((x, y))

    if (x, y) == destino:
        return True

    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        novo_x, novo_y = x + dx, y + dy
        if labirinto_backtracking(maze, novo_x, novo_y, caminho, visitado, destino):
            return True

    caminho.pop()
    visitado[x][y] = False
    return False

if __name__ == "__main__":
    labirinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    caminho = []
    visitado = [[False] * len(labirinto[0]) for _ in range(len(labirinto))]
    destino = (4, 4)

    if labirinto_backtracking(labirinto, 0, 0, caminho, visitado, destino):
        print("Caminho encontrado:", caminho)
    else:
        print("Nenhum caminho encontrado.")
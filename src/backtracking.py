def labirinto_backtracking(maze, x, y, caminho, visitado, destino):
    """
    Resolve um labirinto usando o algoritmo de backtracking iterativo (sem recursão).
    :param maze: Matriz representando o labirinto (0 = caminho, 1 = parede).
    :param x: Coordenada x inicial.
    :param y: Coordenada y inicial.
    :param caminho: Lista para armazenar o caminho percorrido.
    :param visitado: Matriz de controle de células visitadas.
    :param destino: Tupla (x, y) da posição de destino.
    :return: True se o caminho até a saída for encontrado, False caso contrário.
    """
    linhas, colunas = len(maze), len(maze[0])
    pilha = [((x, y), [(x, y)])]  # Pilha com ((x, y), caminho percorrido)

    while pilha:
        (x_atual, y_atual), caminho_atual = pilha.pop()

        if x_atual < 0 or y_atual < 0 or x_atual >= linhas or y_atual >= colunas:
            continue
        
        if maze[x_atual][y_atual] == 1 or visitado[x_atual][y_atual]:
            continue

        visitado[x_atual][y_atual] = True

        if (x_atual, y_atual) == destino:
            caminho.extend(caminho_atual)
            return True

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:  # baixo, direita, cima, esquerda
            novo_x, novo_y = x_atual + dx, y_atual + dy
            nova_rota = caminho_atual + [(novo_x, novo_y)]
            pilha.append(((novo_x, novo_y), nova_rota))

    return False

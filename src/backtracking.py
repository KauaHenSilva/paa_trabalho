def labirinto_backtracking(maze, x, y, caminho, visitado, destino):
    
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

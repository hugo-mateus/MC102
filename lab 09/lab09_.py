def print_matriz(matrix: list[list[int]], espacado = True) -> None:
    """dá print na matriz, com um espaço entre elementos"""
    if espacado:
        print()
    for linha in matrix:
        for i in range(len(linha)):
            print(linha[i], end = '')
            if i< len(linha) - 1:
                print(' ', end = '')
        print()

def posicao_robo(matrix: list[list[int]]) -> list[int]:
    """encontra a posição do robô na matriz"""
    for a in range(len(matrix)):
        for s in range(len(matrix[0])):
            if matrix[a][s] == "r":
                posicao = [a,s]
                return posicao


def escaneamento_de_ambiente(matrix: list[list[int]], pos: list[int]) -> None:
    """ muda a posição do robô para a direita caso a linha for par, para a esquerda
    se a linha for ímpar, e para baixo se o robô estiver no fim da linha"""
    matrix[pos[0]][pos[1]] = "."
    if pos[0] % 2 == 0:
        if pos[1] == len(matrix[0])-1:
        #se o robo estiver no final da linha
            matrix[pos[0] + 1][pos[1]] = "r"
        else:
            matrix[pos[0]][pos[1] + 1] = "r"
    else:
        if pos[1] == 0:
            matrix[pos[0] + 1][pos[1]] = "r"
        else:
            matrix[pos[0]][pos[1] - 1] = "r"
    print_matriz(matrix)

def ficar_no_escaneamento(matrix: list[list[int]], pos: list[int]) -> list[int]:
    """ Encontra as coordenadas para a qual o robô iria caso o escaneamento fosse ocorrer""" 
    if pos[0] % 2 == 0:
        if pos[1] == len(matrix[0])-1:
            return [pos[0] + 1, pos[1]]
        else:
            return [pos[0], pos[1] + 1]
    else:
        if pos[1] == 0:
            return [pos[0] + 1, pos[1]]
        else:
            return [pos[0], pos[1] - 1]

def mudar_de_modulo(matrix: list[list[int]], pos: list[int]) -> list[int]:
    """Descobre se existe sujeira na adjacência do robô, se não tiver, retorna False, se tiver
    retorna as coordenadas em que a sujeira está"""
    if pos[1] > 0:
        if matrix[pos[0]][pos[1]-1] == "o":
            return [pos[0], pos[1]-1]
    if pos[0] > 0:
        if matrix[pos[0]- 1][pos[1]] == "o":
            return [pos[0]-1, pos[1]]
    if pos[1] < len(matrix[0]) - 1:
        if matrix[pos[0]][pos[1] + 1] == "o":
            return [pos[0], pos[1] + 1]
    if pos[0] < len(matrix)- 1:
        if matrix[pos[0]+1][pos[1]] == "o":
            return [pos[0]+1, pos[1]]
    return False


def limpando(matrix: list[list[int]], novas_coordenadas: list[int], pos: list[int]) -> None:
    """Troca a posição do robô para a coordenada onde a sujeira está"""
    matrix[novas_coordenadas[0]][novas_coordenadas[1]] = "r"
    matrix[pos[0]][pos[1]] = "."
    print_matriz(matrix)

def retornar(matrix: list[list[int]], posicao_inicial: list[int], pos: list[int]) -> None:
    """Muda a posição do robô para a coordenada onde ele estava antes de entrar no módulo limpando"""
    while pos[1] > posicao_inicial[1]:
        matrix[pos[0]][pos[1] - 1] = "r"
        matrix[pos[0]][pos[1]] = "."
        pos[1] -= 1
        print_matriz(matrix)
    while pos[1] < posicao_inicial[1]:
        matrix[pos[0]][pos[1] + 1] = "r"
        matrix[pos[0]][pos[1]] = "."
        pos[1] += 1
        print_matriz(matrix)
    while pos[0] > posicao_inicial[0]:
        matrix[pos[0]-1][pos[1]] = "r"
        matrix[pos[0]][pos[1]] = "."
        pos[0] -= 1
        print_matriz(matrix)
    while pos[0] < posicao_inicial[0]:
        matrix[pos[0] +1][pos[1]] = "r"
        matrix[pos[0]][pos[1]] = "."
        pos[1] += 1
        print_matriz(matrix)


def posicoes_diferentes(matrix: list[list[int]], pos: list[int]) -> bool:
    """Booleano que compara as coordenadas onde o robô iria se entrasse no módulo limpando e se 
    continuasse no módulo escaneamento de ambientes, retorna Truese as posições finais forem diferentes"""
    return mudar_de_modulo(matrix, pos) != ficar_no_escaneamento(matrix, pos)

def ir_ao_final_linha(matrix: list[list[int]], pos: list[int]) -> None:
    """Troca a posição do robô para a direita até ele chegar no final da linha"""
    for a in range(len(matrix)):
        matrix[pos[0]][pos[1]] = "."
        matrix[pos[0]][pos[1]+ 1] = "r"
        print_matriz(matrix)
        pos = posicao_robo(matrix)

def main():
    linhas = int(input())
    matrix = []
    for i in range(linhas):
        linha = input().split()
        matrix.append(linha)
    print_matriz(matrix, False)
    chegou_no_canto = False
    pos  = posicao_robo(matrix)
    while not (chegou_no_canto and pos == [linhas -1, len(matrix[0])- 1]):
        pos  = posicao_robo(matrix)
        if pos == [linhas-1, 0]:
            chegou_no_canto = True
        novas_coordenadas = mudar_de_modulo(matrix, pos)
        if linhas % 2 == 0 and pos[0] == linhas -1 and chegou_no_canto:
            ir_ao_final_linha(matrix, pos)
            break
        posicao_inicial = pos
        while novas_coordenadas != False and posicoes_diferentes(matrix, pos):
            limpando(matrix, novas_coordenadas, pos)
            pos = posicao_robo(matrix)
            novas_coordenadas = mudar_de_modulo(matrix, pos)
        retornar(matrix, posicao_inicial, pos)
        escaneamento_de_ambiente(matrix, pos)
        pos  = posicao_robo(matrix)

if __name__ == '__main__':
    main()
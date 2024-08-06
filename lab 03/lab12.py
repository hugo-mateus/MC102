###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Pac-Man I
# Nome:Guilherme Antunes Fogaça
# RA:252356
###################################################

class Mapa:
    def __init__(self, matriz, posicao_poder, posicao_paredes, posicao_fantasmas, posicao_pastilhas):
        self.matriz = matriz
        self.posicao_poder = posicao_poder
        self.posicao_paredes = posicao_paredes
        self.posicao_fantasmas = posicao_fantasmas
        self.posicao_pastilhas = posicao_pastilhas

class Packman:
    def __init__(self, posicao, vivo, quantidade_coletada, imortal, direcao, poder_duracao):
        self.posicao = posicao
        self.vivo = vivo
        self.quantidade_coletada = quantidade_coletada
        self.imortal = imortal
        self.direcao = direcao
        self.poder_duracao = poder_duracao

def ler_matriz(n):
    matriz = []
    for _ in range(n):
        linha = input().strip().split()
        linha = list(linha[0])
        matriz.append(linha)
    return matriz

def achar(matriz, coisa):
    lugar = []
    for m in range(len(matriz)):
        for n in range(len(matriz[0])):
            if matriz[m][n] == coisa:
                lugar.append([m, n])
    return lugar

def pode_andar(posicao_packman):
    pode = True
    for i in range(len(Mapa.posicao_paredes)):
        if Mapa.posicao_paredes[i] == posicao_packman:
            pode = False
    return pode

def andar_direita():
    if (Packman.direcao == ">" and pode_andar([Packman.posicao[0]+1, Packman.posicao[1]])):
        Packman.posicao[0] +=1
        Packman.direcao = ";"
        return True
    if (Packman.direcao == "<" and pode_andar([Packman.posicao[0]-1, Packman.posicao[1]])):
        Packman.posicao[0] -=1
        Packman.direcao = "^"
        return True
    if (Packman.direcao == "^" and pode_andar([Packman.posicao[0], Packman.posicao[1]+1])):
        Packman.posicao[1] += 1
        Packman.direcao = ">"
        return True
    if (Packman.direcao == ";" and pode_andar([Packman.posicao[0], Packman.posicao[1]-1])):
        Packman.posicao[1] -=1
        Packman.direcao = "<"
        return True
    return False

def andar_esquerda():
    if (Packman.direcao == ">" and pode_andar([Packman.posicao[0]-1, Packman.posicao[1]])):
        Packman.posicao[0] -=1
        Packman.direcao = "^"
        return True
    if (Packman.direcao == "<" and pode_andar([Packman.posicao[0]+1, Packman.posicao[1]])):
        Packman.posicao[0] +=1
        Packman.direcao = ";"
        return True
    if (Packman.direcao == "^" and pode_andar([Packman.posicao[0], Packman.posicao[1]-1])):
        Packman.posicao[1] -= 1
        Packman.direcao = "<"
        return True
    if (Packman.direcao == ";" and pode_andar([Packman.posicao[0], Packman.posicao[1]+1])):
        Packman.posicao[1] +=1
        Packman.direcao = ">"
        return True
    return False

def andar_frente():
    if (Packman.direcao == ">" and pode_andar([Packman.posicao[0], Packman.posicao[1]+1])):
        Packman.posicao[1] +=1
        return True
    if (Packman.direcao == "<" and pode_andar([Packman.posicao[0], Packman.posicao[1]-1])):
        Packman.posicao[1] -=1
        return True
    if (Packman.direcao == "^" and pode_andar([Packman.posicao[0]-1, Packman.posicao[1]])):
        Packman.posicao[0] -= 1
        return True
    if (Packman.direcao == ";" and pode_andar([Packman.posicao[0]+1, Packman.posicao[1]])):
        Packman.posicao[0] +=1
        return True
    return False

def andar_voltando():
    if (Packman.direcao == ">" and pode_andar([Packman.posicao[0], Packman.posicao[1]-1])):
        Packman.posicao[1] -=1
        Packman.direcao = "<"
        return True
    if (Packman.direcao == "<" and pode_andar([Packman.posicao[0], Packman.posicao[1]+1])):
        Packman.posicao[1] +=1
        Packman.direcao = ">"
        return True
    if (Packman.direcao == "^" and pode_andar([Packman.posicao[0]+1, Packman.posicao[1]])):
        Packman.posicao[0] += 1
        Packman.direcao = ";"
        return True
    if (Packman.direcao == ";" and pode_andar([Packman.posicao[0]-1, Packman.posicao[1]])):
        Packman.posicao[0] -=1
        Packman.direcao = "^"
        return True
    return False

def pegando_pastilhas():
    for q in range(len(Mapa.posicao_pastilhas)):
            if(Mapa.posicao_pastilhas[q] == Packman.posicao):
                Packman.quantidade_coletada += 1
                Mapa.posicao_pastilhas.pop(q)
                break

def pegando_poder():
    if(Packman.imortal > 0):
            Packman.imortal -= 1
    for w in range(len(Mapa.posicao_poder)):
                if(Mapa.posicao_poder[w] == Packman.posicao):
                    Packman.imortal = Packman.poder_duracao +1
                    Packman.quantidade_coletada += 1
                    Mapa.posicao_poder.pop(w)
                    break

def encontrando_fantasmas():
    for e in range(len(Mapa.posicao_fantasmas)):
            if(Mapa.posicao_fantasmas[e] == Packman.posicao and Packman.imortal == 0):
                Packman.vivo = False

def packman_andando():
    andou = andar_direita()
    if(andou == False):
        andou = andar_frente()
    if(andou == False):
        andou = andar_esquerda()
    if(andou == False):
        andou = andar_voltando()


def main():
    linhas = int(input())
    poder_duracao = int(input())

    Mapa.matriz = ler_matriz(linhas)
    Mapa.posicao_fantasmas = achar(Mapa.matriz, "X")
    Mapa.posicao_poder = achar(Mapa.matriz, "*")
    Mapa.posicao_paredes = achar(Mapa.matriz,"#")
    Mapa.posicao_pastilhas = achar(Mapa.matriz, ".")

    Packman.posicao = achar(Mapa.matriz, "C")
    Packman.posicao = Packman.posicao[0]
    Packman.vivo = True
    Packman.quantidade_coletada = 0
    Packman.imortal = 0
    Packman.direcao = ">" #> < ^ ;
    Packman.poder_duracao = poder_duracao

    while(Packman.vivo == True and len(Mapa.posicao_pastilhas) > 0):
        packman_andando()
        pegando_pastilhas()
        pegando_poder()
        encontrando_fantasmas()
        

    print(Packman.quantidade_coletada)


if __name__ == "__main__":
    main()

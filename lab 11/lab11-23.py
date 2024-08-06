class Mapa:
    def __init__(self, tamanho, saida, posicao_link, posicao_objetos, posicao_monstos):
        self.tamanho = tamanho
        self.saida = saida
        self.posicao_link = posicao_link
        self.posicao_objetos = posicao_objetos
        self.posicao_monstos = posicao_monstos


class Link:
    def __init__(self, pv,dano):
        self.pv = pv
        self.dano = dano


def inputs_listas(classe, sep):
    """pega os inputs e armazana-os em classes"""
    var = input().split(sep)
    classe.append(int(var[0]))
    classe.append(int(var[1]))
    return classe


def imprimir(monstros_d, objetos_d, letra):
    """imprime a matriz"""
    imprimidos = 0
    linhas = 0
    colunas = 0
    for r in range(Mapa.tamanho[0]* Mapa.tamanho[1]):
        quebrar = False
        if imprimidos % Mapa.tamanho[1] == 0 and imprimidos != 0:
            linhas += 1
            colunas = 0
        #posicao Link
        if Mapa.posicao_link == [linhas, colunas]:
            if Mapa.posicao_link[1] == Mapa.tamanho[1] - 1:
                print(letra)
            else:
                print( letra, end=' ')
            imprimidos += 1
            colunas += 1
            quebrar = True
        #saida
        if not quebrar:
            if Mapa.saida == [linhas, colunas]:
                if Mapa.saida[1] == Mapa.tamanho[1]-1:
                    print("*")
                else:
                    print("*", end=' ')
                imprimidos += 1
                colunas += 1
                quebrar = True
        #monstros
        if not quebrar: 
            imprimir = False
            aux_3 = False
            for y in monstros_d:
                aux = monstros_d[y]
                if aux[3] == str(linhas) + "," + str(colunas):
                    imprimir = aux[2]
                    aux_3 = aux[3]
            if imprimir != False:
                auxs = aux_3.split(",")
                if int(auxs[1]) == Mapa.tamanho[1] -1:
                    print(imprimir)
                else:
                    print(imprimir, end=' ')
                imprimidos += 1
                colunas += 1
                quebrar = True
        #objetos
        if not quebrar:
            imprimir = False
            aux_2 = False
            for u in objetos_d:
                aux = objetos_d[u]
                if aux[2] == str(linhas) + "," + str(colunas):
                    imprimir = aux[1]
                    aux_2 = aux[2]
            if imprimir != False:
                auxs = aux_2.split(",")
                if int(auxs[1])  == Mapa.tamanho[1]-1:
                    print(imprimir)
                else:
                    print(imprimir, end=' ')
                imprimidos += 1
                colunas += 1
                quebrar = True
        if not quebrar:
            if colunas == Mapa.tamanho[1]-1:
                print(".")
            else:         
                print(".", end=' ')
            imprimidos += 1
            colunas += 1


def movimentar_monstros(monstros_d):
    """modifica as coordenadas dos monstros conforme sua movimentacao"""
    for i in monstros_d:
        aux = monstros_d[i]
        posicao = aux[3].split(",")
        if aux[2] == "U":
            if int(posicao[0]) != 0:
                monstros_d[i] = [aux[0], aux[1],  aux[2], str(int(posicao[0]) -1) + "," + str(posicao[1])]
        if aux[2] == "D":
            if int(posicao[0]) != Mapa.tamanho[0]-1:
                monstros_d[i] = [aux[0], aux[1],  aux[2], str(int(posicao[0]) + 1) + "," + str(posicao[1])]
        if aux[2] == "L":
            if int(posicao[1]) != 0:
                monstros_d[i] = [aux[0], aux[1],  aux[2], str(posicao[0]) + "," + str(int(posicao[1]) - 1)]
        if aux[2] == "R":
            if int(posicao[1]) != Mapa.tamanho[1]-1:
                monstros_d[i] = [aux[0], aux[1],  aux[2], str(posicao[0]) + "," + str(int(posicao[1]) + 1)]


def movimentacao_link(chegou_na_ultima):
    """modifica a posicao do link conforme a sua movimentacao"""
    if chegou_na_ultima == False:
        aux = Mapa.posicao_link
        Mapa.posicao_link = [aux[0] + 1,aux[1]]
    else:
        aux = Mapa.posicao_link
        if int(aux[0]) % 2 == 0: #esta em linha par
            if int(aux[1]) != 0:
                Mapa.posicao_link = [aux[0],aux[1] -1]
            else:
                Mapa.posicao_link = [aux[0] -1, aux[1]]
        else:
            if int(aux[1]) != (Mapa.tamanho[1]-1):
                Mapa.posicao_link = [aux[0],aux[1] +1]
            else:
                Mapa.posicao_link = [aux[0] -1,aux[1]]


def pegar_objeto(objetos_d):
    """Muda os atributos do Link dependendo dos objetos adquiridos e os retira do mapa"""
    for a in objetos_d:
        aux = objetos_d[a]
        if str(Mapa.posicao_link[0]) + "," + str(Mapa.posicao_link[1])  == aux[2]:
            if aux[1] == "d":
                objetos_d[a] = [aux[0], ".", aux[2], aux[3]]
                dano_inicial = Link.dano
                Link.dano = dano_inicial + int(aux[3])
                print("[d]Personagem adquiriu o objeto", aux[0], "com status de", aux[3])
            if aux[1] ==  "v":
                objetos_d[a] = [aux[0], ".", aux[2], aux[3]]
                vida_inicial = Link.pv
                Link.pv = vida_inicial + int(aux[3])
                print("[v]Personagem adquiriu o objeto", aux[0], "com status de", aux[3])


def lutando_monstros(monstros_d, objetos_d):
    """Muda a vida de acordo com o dano, tanto dos monstros quanto do Link,
    e faz os prints das informações da luta"""
    for i in monstros_d:
        aux = monstros_d[i]
        if (str(Mapa.posicao_link[0]) + "," + str(Mapa.posicao_link[1])  == aux[3]) and int(aux[0]) > 0:
            #se estiverem na mesma posicao
            pv_inicial = Link.pv
            if Link.dano >= 1:
                aux[0] = int(aux[0]) - Link.dano
            else:
                aux[0] = int(aux[0]) - 1
            if aux[0] > 0:
                Link.pv -= int(aux[1])
            if Link.dano >= 1:
                print("O Personagem deu ", Link.dano, " de dano ao monstro na posicao (", Mapa.posicao_link[0], ", ", Mapa.posicao_link[1], ")", sep ='')
            else:
                print("O Personagem deu 1 de dano ao monstro na posicao (", Mapa.posicao_link[0], ", ", Mapa.posicao_link[1], ")", sep ='')
            if Link.pv > 0 and aux[0] > 0:
                print("O Monstro deu", aux[1], "de dano ao Personagem. Vida restante =", Link.pv)
            elif aux[0] > 0:
                print("O Monstro deu", pv_inicial, "de dano ao Personagem. Vida restante = 0")
            if aux[0] <= 0:
                monstros_d[i] = [aux[0], aux[1], ".", aux[3]]
            if Link.pv <= 0:
                imprimir(monstros_d, objetos_d, "X")


def main():
    #armazenando inputs
    vp_dp = input().split(" ")
    Link.pv = int(vp_dp[0])
    Link.dano = int(vp_dp[1])
    Mapa.tamanho = []
    inputs_listas(Mapa.tamanho, " ")
    Mapa.posicao_link = []
    inputs_listas(Mapa.posicao_link, ",")
    Mapa.saida = []
    inputs_listas(Mapa.saida, ",")
    quantidade_monstros = int(input())
    monstros_d = {}
    for q in range(quantidade_monstros):
        especificos_monstros = input().split(" ")
        monstros_d[q] = especificos_monstros
    quantidade_objetos = int(input())
    objetos_d = {}
    for w in range(quantidade_objetos):
        especificos_objetos = input().split(" ")
        objetos_d[w] = especificos_objetos


    chegou_na_ultima = False
    posicoes_iguais = False

    while not(posicoes_iguais) and Link.pv > 0 : 
        imprimir(monstros_d, objetos_d, "P")
        print()
        movimentar_monstros(monstros_d)
        if Mapa.posicao_link[0] == (Mapa.tamanho[0]-1):
            chegou_na_ultima = True
            #encontra se Link já chegou na ultima linha para mudar a sua movimentacao
        movimentacao_link(chegou_na_ultima)
        pegar_objeto(objetos_d)
        if Mapa.posicao_link == Mapa.saida:
            #se ele chega ao final após sua movimentacao
            imprimir(monstros_d, objetos_d, "P")
            print()
            posicoes_iguais = True
            print("Chegou ao fim!")
        lutando_monstros(monstros_d, objetos_d)


if __name__ == '__main__':
    main()

def ordenar_mao(lista):
    prioridades_primeiro = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
    prioridades_segundo = ['P', 'C', 'E', 'O']

    lista_separada = []
    for item in lista:
        for x in item:
            if x == "1":
                lista_separada.append("10")
            elif x != "0":
                lista_separada.append(x)

    lista_primeiros = []
    for r in range(len(lista_separada)):
        if r % 2 == 0:
            lista_primeiros.append(lista_separada[r])

    lista_segundos = []
    for r in range(len(lista_separada)):
        if r % 2 != 0:
            lista_segundos.append(lista_separada[r])
    bubblesort_1(lista_primeiros,prioridades_primeiro, lista_segundos)
    bubblesort_2(lista_segundos, prioridades_segundo, lista_primeiros) 

    lista = []
    for t in range(len(lista_primeiros)):
        lista.append(lista_primeiros[t]+ lista_segundos[t])
    return lista


def bubblesort_1(lista, lista_prioridades, listas_segundo):
    for i in range(len(lista) - 1):
        trocou = False
        for j in range(len(lista) - 1, i, -1):
            if lista_prioridades.index(lista[j - 1]) > lista_prioridades.index(lista[j]):
                trocou = True
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
                #muda na segunda lista
                aux = listas_segundo[j]
                listas_segundo[j] = listas_segundo[j - 1]
                listas_segundo[j - 1] = aux
        if not trocou:
            break
    return lista, listas_segundo


def bubblesort_2(lista, lista_prioridades, listas_primeiro):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1, i, -1):
            if lista_prioridades.index(lista[j - 1]) > lista_prioridades.index(lista[j]):
                if listas_primeiro[j] == listas_primeiro[j-1]:
                    aux = lista[j]
                    lista[j] = lista[j - 1]
                    lista[j - 1] = aux
                    #muda na segunda lista
                    aux = listas_primeiro[j]
                    listas_primeiro[j] = listas_primeiro[j - 1]
                    listas_primeiro[j - 1] = aux
    return lista, listas_primeiro


def ordenar_primeiros_caracteres(lista):
    lista_separada = []
    for item in lista:
        for x in item:
            if x == "1":
                lista_separada.append("10")
            elif x != "0":
                lista_separada.append(x)

    lista_primeiros = []
    for r in range(len(lista_separada)):
        if r % 2 == 0:
            lista_primeiros.append(lista_separada[r])

    prioridades_primeiro = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    for i in range(len(lista) - 1):
        trocou = False
        for j in range(len(lista) - 1, i, -1):
            if prioridades_primeiro.index(lista[j - 1]) > prioridades_primeiro.index(lista[j]):
                trocou = True
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
        if not trocou:
            break
    return lista

def pegar_valor(lista):
    lista_separada = []
    for item in lista:
        for x in item:
            if x == "1":
                lista_separada.append("10")
            elif x != "0":
                lista_separada.append(x)

    lista_primeiros = []
    for r in range(len(lista_separada)):
        if r % 2 == 0:
            lista_primeiros.append(lista_separada[r])
    return lista_primeiros


def lista_para_string(lista):
    elementos = [str(item) for item in lista]
    resultado = " ".join(elementos)
    return resultado


def rodada(jogadores, pilha, rodadas):
    cartas_jogadas = []
    p = 0
    if p <= rodadas:
        for x in jogadores:
            achou = False
            r = 0
            for i in range(len(jogadores[x])):
                while not achou:
                    aux = jogadores[x]
                    possivel = cartas_jogadas[:]
                    possivel.append(aux[-1-r])
                    copia_possivel = possivel[:]
                    ordenar_primeiros_caracteres(possivel).reverse()
                    if possivel == copia_possivel:
                        valores = pegar_valor(aux)
                        valor_selecionado = valores[r]
                        cartas_jogadas = 0
                        for t in valores:
                            if t == valores[r]:
                                pilha.append(aux[t])
                                cartas_jogadas += 1
                        achou = True
                    r += 1
                print("[Jogador", x,"]",end ='')
                print(cartas_jogadas, "carta(s)", end ='')
                print("Pilha:", lista_para_string(pilha))
                p += 1


def main():
    n_jogadores = int(input())
    jogadores = {}
    #forma dicionario com listas {1: [], 2:[]}
    for q in range(n_jogadores):
        aux = input(). split(", ")
        aux = ordenar_mao(aux)
        jogadores[q] = aux
    rodadas = int(input())
    vencido = False
    pilha = []
    while not vencido:
        for w in jogadores:
            print("Jogador", w+1)
            print("Mão:", lista_para_string(jogadores[w])) 
        r = 0
        for e in range(rodadas):
            print("Pilha:", lista_para_string(pilha)) 
            r += 1
            if r > n_jogadores:
                n = 1
            #funcao p descobri q carta q ele vai jogar
            print("[Jogador", r, "]")
            if e == rodadas-1:
                print("Jogador", r-1, "duvidou.")
                #duvida
        for r in jogadores:
            if jogadores[r] == []:
                vencido = True
        vencido = True #tirar
                
main()
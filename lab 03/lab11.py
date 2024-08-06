###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Níveis de Radiação
# Nome:Guilherme Antunes Fogaça
# RA:25235
###################################################

def ler_matriz(n):
    matriz = []
    for _ in range(n):
        linha = input().strip().split()
        linha = list(linha[0])
        matriz.append(linha)
    return matriz

def tranformar_em_int(matriz_inicial):
    for m in range(len(matriz_inicial)):
        for n in range(len(matriz_inicial[0])):
            matriz_inicial[m][n] = int(matriz_inicial[m][n])
    return matriz_inicial

def tranformar_em_str(matriz_inicial):
    for m in range(len(matriz_inicial)):
        for n in range(len(matriz_inicial[0])):
            matriz_inicial[m][n] = str(matriz_inicial[m][n])
    return matriz_inicial

def achar_radiacao(matriz_inicial):
    lugar_radiacao = []
    for m in range(len(matriz_inicial)):
        for n in range(len(matriz_inicial[0])):
            if matriz_inicial[m][n] != 0:
                lugar_radiacao.append([matriz_inicial[m][n], m, n])
    return lugar_radiacao

def criar_matriz_vazia (matriz_inicial):
    matriz_vazia = []
    matriz_aux = []
    for m in range(len(matriz_inicial)+1):
        if matriz_aux != []:
            matriz_vazia.append(matriz_aux)
        matriz_aux = []
        for n in range(len(matriz_inicial[0])):
            matriz_aux.append(0)
    return matriz_vazia

def somar_matrizes(matriz_1, matriz_2):
    for m in range(len(matriz_1)):
        for n in range(len(matriz_1[0])):
            matriz_1[m][n] += matriz_2[m][n]
    return matriz_1

def printar_matriz(matriz_vazia):
    matriz_vazia = tranformar_em_str(matriz_vazia)
    for o in range(len(matriz_vazia)):
        print(''.join(matriz_vazia[o]))

def propagar_radiacao(matriz_vazia, linha_radiacao, valor_radiacao):
    for i in range(linha_radiacao[0]):
        for j in range(linha_radiacao[0]):
            if (linha_radiacao[1]-i >= 0 and linha_radiacao[2] >= 0 and
                linha_radiacao[1]-i < len(matriz_vazia) and linha_radiacao[2] < len(matriz_vazia[0])):
                matriz_vazia[linha_radiacao[1]-i][linha_radiacao[2]] = valor_radiacao

            if (linha_radiacao[1] >= 0 and linha_radiacao[2]-j >= 0 and 
                linha_radiacao[1] < len(matriz_vazia) and linha_radiacao[2]-j < len(matriz_vazia[0])):
                matriz_vazia[linha_radiacao[1]][linha_radiacao[2]-j] = valor_radiacao

            if (((linha_radiacao[1]-linha_radiacao[0]+1 >= 0) and 
                (linha_radiacao[2]-j >= 0)) and ((linha_radiacao[1]-linha_radiacao[0]+1) < len(matriz_vazia)) and ((linha_radiacao[2]-j) < len(matriz_vazia[0]))):
                matriz_vazia[linha_radiacao[1]-linha_radiacao[0]+1][linha_radiacao[2]-j] = valor_radiacao
            
            if (((linha_radiacao[1]-i) >= 0) and linha_radiacao[2]-linha_radiacao[0]+1 >= 0 and 
                linha_radiacao[1]-i < len(matriz_vazia) and ((linha_radiacao[2]-linha_radiacao[0]+1) < len(matriz_vazia[0]))):
                matriz_vazia[linha_radiacao[1]-i][linha_radiacao[2]-linha_radiacao[0]+1] = valor_radiacao
    return matriz_vazia

def propaga_radiacao(matriz_vazia, linha_radiacao):
    valor_radiacao = linha_radiacao[0]
    v = valor_radiacao
    for i in range(v):
        if i >0:
            linha_radiacao[1] = linha_radiacao[1]+1
            linha_radiacao[2] = linha_radiacao[2]+1
        linha_radiacao[0] = ((i+1)*2)-1
        matriz_vazia = propagar_radiacao(matriz_vazia, linha_radiacao, valor_radiacao)
        valor_radiacao -= 1
    return matriz_vazia

def acha_radiacao_alta(matriz_vazia):
    for m in range(len(matriz_vazia)):
        for n in range(len(matriz_vazia[0])):
            if matriz_vazia[m][n] >9:
                matriz_vazia[m][n]= "+"

def main():
    #pegando input
    l = int(input())
    matriz_inicial = ler_matriz(l)
    matriz_inicial = tranformar_em_int(matriz_inicial)

    #achando os lugar de radiacao
    #lugar_radiacao = matriz com len =num de lugares com radiacao
    #cada linha da matriz lugar_radiacao [num da radiacao, l, c]
    lugar_radiacao = achar_radiacao(matriz_inicial)


    matriz_vazia = criar_matriz_vazia(matriz_inicial)


    for i in range(len(lugar_radiacao)):
        matriz_aux = criar_matriz_vazia(matriz_inicial)
        matriz_aux = propaga_radiacao(matriz_aux, lugar_radiacao[i])
        matriz_vazia = somar_matrizes(matriz_vazia, matriz_aux)

    acha_radiacao_alta(matriz_vazia)

    printar_matriz(matriz_vazia)

if __name__ == "__main__":
    main()

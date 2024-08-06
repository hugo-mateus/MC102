def separa_caracteres(string) -> list[int]:
    lista_fim = []
    for i in string:
        for j in i:
                lista_fim.append(j)
    return lista_fim


def descobrir_index(ASCCI_completa,caracter):
    for v in range(len(ASCCI_completa)):
        if caracter in ASCCI_completa[v]:
            return int(v)


def descobrir_operador(operando):
    if operando == "numero":
        for v in range(len(linhas_completo)):
            for r in range(len(ASCCI_numeros)):
                if ASCCI_numeros[r] in linhas_completo[v]:
                    return linhas_completo.index(linhas_completo[v])
    if operando == "vogal":
        for v in range(len(linhas_completo)):
            for r in range(len(vogais)):
                if vogais[r] in linhas_completo[v]:
                    return linhas_completo.index(linhas_completo[v])
    if operando == "consoante":
        for v in range(len(linhas_completo)):
            for r in range(len(consoantes)):
                if consoantes[r] in linhas_completo[v]:
                    return linhas_completo.index(linhas_completo[v])
    else:
        for v in range(len(linhas_completo)):
            if operando in linhas_completo[v]:
                return linhas_completo.index(linhas_completo[v])


def calcular_chave(operador_1, operador_2, operador):
    if operador == "+":
        return operador_1 + operador_2
    if operador == "-":
        return operador_1 - operador_2
    if operador == "*":
        return operador_1 * operador_2


def imprimir_lista_como_string(lista):
    for a in range(len(lista)):
        for b in range(len(lista[a])):
            print(lista[a][b], end = '')
        print("")
    return ""


def descobrir_lista_decriptada(mensagem_por_linhas, ASCCI_completa):
    resultado_completo = []
    resultado_parcial = []
    for i in range(len(mensagem_por_linhas)):
        for r in range(len(mensagem_por_linhas[i])): 
            caracter = mensagem_por_linhas[i][r]
            indice_na_ASCCI = descobrir_index(ASCCI_completa, caracter)
            novo_indice = indice_na_ASCCI + chave
            while novo_indice >= 95:
                novo_indice = novo_indice - 95
            resultado_parcial.append(ASCCI_completa[novo_indice])
        resultado_completo.append(resultado_parcial)
        resultado_parcial = []
    return resultado_completo

ASCCI_32 = [" "]
ASCCI_32_a_47 = separa_caracteres("!\"#$%&'()*+,-./")
ASCCI_numeros = separa_caracteres("0123456789")
ASCCI_58_a_64 = separa_caracteres(":;<=>?@")
ASCCI_letras_maisculas = separa_caracteres("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ASCCI_91_a_96 = separa_caracteres("[\\]^_`") 
ASCCI_letras_minusculas = separa_caracteres("abcdefghijklmnopqrstuvwxyz")
ASCCI_123_a_126 = separa_caracteres("{|}~")
vogais = separa_caracteres("AEIOUaeiou")
consoantes = separa_caracteres("bcdfghjklmnpqrstvBCDFGHJKLMNPQRSTVWXYZ")
ASCCI_completa = []
ASCCI_completa.extend(ASCCI_32)
ASCCI_completa.extend(ASCCI_32_a_47)
ASCCI_completa.extend(ASCCI_numeros)
ASCCI_completa.extend(ASCCI_58_a_64)
ASCCI_completa.extend(ASCCI_letras_maisculas)
ASCCI_completa.extend(ASCCI_91_a_96)
ASCCI_completa.extend(ASCCI_letras_minusculas)
ASCCI_completa.extend(ASCCI_123_a_126)

operador = input()
operando1 = input()
operando2 = input()
numero_linhas = int(input())
linhas_completo = []
mensagem_por_linhas = []
for i in range(numero_linhas):
    linhas = separa_caracteres(input())
    mensagem_por_linhas.append(linhas)
    for v in range(len(linhas)):
        linhas_completo.append(linhas[v])

operador_1 = descobrir_operador(operando1)
operador_2 = descobrir_operador(operando2)

chave = calcular_chave(operador_1,operador_2, operador)
print(chave)

lista_decriptada = descobrir_lista_decriptada(mensagem_por_linhas, ASCCI_completa)
imprimir_lista_como_string(lista_decriptada)



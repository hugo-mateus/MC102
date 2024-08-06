def aumenta_tamanho(lista_1: list[int], lista_2: list[int], n: int) -> None:
    tamanho = len(lista_1) - len(lista_2)
    for i in range(tamanho):
        lista_2.append(n)


def soma_vetores(lista_1: list[int], lista_2: list[int]) -> list[int]:
    aumenta_tamanho(lista_2, lista_1, 0)
    aumenta_tamanho(lista_1, lista_2, 0)
    lista_resultante = []
    for n in range(len(lista_1)):
        lista_resultante.append(lista_1[n] + lista_2[n])
    return lista_resultante


def subtrai_vetores(lista_1: list[int], lista_2: list[int]) -> list[int]:
    aumenta_tamanho(lista_2, lista_1, 0)
    aumenta_tamanho(lista_1, lista_2, 0)
    lista_resultante = []
    for n in range(len(lista_1)):
        lista_resultante.append(lista_1[n] - lista_2[n])
    return lista_resultante


def multiplica_vetores(lista_1: list[int], lista_2: list[int]) -> list[int]:
    aumenta_tamanho(lista_2, lista_1, 1)
    aumenta_tamanho(lista_1, lista_2, 1)
    lista_resultante = []
    for n in range(len(lista_1)):
        lista_resultante.append(lista_1[n] * lista_2[n])
    return lista_resultante


def divide_vetores(lista_1: list[int], lista_2: list[int]) -> list[int]:
    aumenta_tamanho(lista_2, lista_1, 0)
    aumenta_tamanho(lista_1, lista_2, 1)
    lista_resultante = []
    for n in range(len(lista_1)):
        lista_resultante.append(int(lista_1[n] // lista_2[n]))
    return lista_resultante


def multiplicacao_escalar(lista: list[int], escalar: int) -> list[int]:
    lista_resultante = []
    for x in range(len(lista)):
        lista_resultante.append(lista[x] * escalar)
    return lista_resultante


def n_duplicacao(lista: list[int], N: int) -> list[int]:
    lista_resultante = []
    for i in range(N):
        for n in range(len(lista)):
            lista_resultante.append(lista[n])
    return lista_resultante


def soma_elementos(lista: list[int]) -> int:
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    lista.clear()
    lista.append(soma)
    return soma


def produto_interno(lista_1: list[int], lista_2: list[int]) -> int:
    aumenta_tamanho(lista_2, lista_1, 1)
    aumenta_tamanho(lista_1, lista_2, 1)
    produto = 0
    for i in range(len(lista_1)):
        produto += lista_1[i] * lista_2[i]
    lista_1.clear()
    lista_1.append(produto)
    return produto


def multiplica_todos(lista_1: list[int], lista_2: list[int]) -> list[int]:
    lista_resultante = []
    elemento = 0
    for i in range(len(lista_1)+1):
        if i > 0:
            lista_resultante.append(elemento)
            elemento = 0
        if i == len(lista_1):
            return lista_resultante
        for x in range(len(lista_2)):
            elemento += lista_1[i] * lista_2[x]
    return lista_resultante


def multiplica_pra_correlacao(lista_1: list[int], lista_2: list[int]) -> int:
    lista_resultante = []
    aux = 0
    for i in range(len(lista_1)):
        aux += lista_1[i] * lista_2[i]
    lista_resultante.append(aux)
    return soma_elementos(lista_resultante)


def correlacao_cruzada(lista_1: list[int], lista_2: list[int]) -> list[int]:
    lista_resultante = []
    for i in range(len(lista_1) - len(lista_2) + 1):
        aux = multiplica_pra_correlacao(lista_2, lista_1[i:len(lista_2)+i])
        lista_resultante.append(aux)
    return lista_resultante


def pegar_lista(vetor: str) -> list[int]:
    return [int(i) for i in vetor.split(",")]


def darprintnalista(lista: list[int]) -> None:
    print("[", end='')
    for i in range(len(lista)):
        if i == len(lista)-1:
            print(lista[i], end='')
        else:
            print(lista[i], end=', ')
    print("]")


def main() -> None:
    lista_vetores = pegar_lista(input())
    comando = input()
    while comando != "fim":
        if comando == "soma_vetores":
            lista_2 = pegar_lista(input())
            lista_vetores = soma_vetores(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        if comando == "subtrai_vetores":
            lista_2 = pegar_lista(input())
            lista_vetores = subtrai_vetores(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        if comando == "multiplica_vetores":
            lista_2 = pegar_lista(input())
            lista_vetores = multiplica_vetores(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        if comando == "divide_vetores":
            lista_2 = pegar_lista(input())
            lista_vetores = divide_vetores(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        if comando == "multiplicacao_escalar":
            escalar = int(input())
            lista_vetores = multiplicacao_escalar(lista_vetores, escalar)
            darprintnalista(lista_vetores)
        if comando == "n_duplicacao":
            n = int(input())
            lista_vetores = n_duplicacao(lista_vetores, n)
            darprintnalista(lista_vetores)
        if comando == "soma_elementos":
            print("[", end='')
            print(soma_elementos(lista_vetores), end='')
            print("]")
        if comando == "produto_interno":
            lista_2 = pegar_lista(input())
            print("[", end='')
            print(produto_interno(lista_vetores, lista_2), end='')
            print("]")
        if comando == "multiplica_todos":
            lista_2 = pegar_lista(input())
            lista_vetores = multiplica_todos(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        if comando == "correlacao_cruzada":
            lista_2 = pegar_lista(input())
            lista_vetores = correlacao_cruzada(lista_vetores, lista_2)
            darprintnalista(lista_vetores)
        comando = input()


if __name__ == "__main__":
    main()


print("\n")

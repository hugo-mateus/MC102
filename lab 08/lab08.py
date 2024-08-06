def armazenar_em_dicionarios(avaliacoes, categoria, strg, e) -> dict:
    """cria um dicionario que deixa como chave os nomes dos filmes, e 
    como valor, uma lista com a quantidade de avaliacoes e as notas recebidas"""
    if avaliacoes[e][1] == strg:
        lista = [1]
        lista.append(int(avaliacoes[e][3]))
        if avaliacoes[e][2] not in categoria:
            categoria[avaliacoes[e][2]] = lista
        else:
            b = categoria[avaliacoes[e][2]]
            b[0] += 1
            b.append(int(avaliacoes[e][3]))
            categoria[avaliacoes[e][2]] = b
    return avaliacoes

def dicionario_com_notas(categoria) -> dict:
    """calcula a media simples com as notas dadas"""
    notas = {}
    for r in categoria:
        b = categoria[r]
        soma = -(b[0])
        for t in range(len(b)):
            soma += b[t]
        nota = soma / (len(b) -1) 
        notas[r] = [b[0], nota]
    return notas


def vencedor_simples(categoria) -> list:
    """Faz uma lista com o vencedor de cada categoria, 
    sua média de notas e quantidade de avaliacoes"""
    maior = [0, 0, 0]
    for y in categoria:
        b = categoria[y]
        if b[1] > maior[1]:
            maior = [y , b[1], b[0]]
        if b[1] == maior[1]:
            if b[0] > maior[2]:
                maior = [y, b[1], b[0]]
    return maior


def main():
    n_filmes = int(input())
    nome_filmes = []
    for q in range(n_filmes):
        nome_filmes.append(input())
    n_avaliacoes = int(input())
    avaliacoes = []
    todas_avaliacoes = []
    for w in range(n_avaliacoes):
        avaliacoes.append(input().split(", "))
        if avaliacoes[w][2] not in todas_avaliacoes:
            todas_avaliacoes.append(avaliacoes[w][2])

    bocejos = {}
    pausado = {}
    revirou = {}
    discussao = {}
    enredo = {}

    for e in range(len(avaliacoes)):
        for r in range(5):
            if r == 0:
                armazenar_em_dicionarios(avaliacoes, bocejos, "filme que causou mais bocejos", e)
            if r == 1:
                armazenar_em_dicionarios(avaliacoes, pausado, "filme que foi mais pausado", e)
            if r == 2:
                armazenar_em_dicionarios(avaliacoes, revirou, "filme que mais revirou olhos", e)
            if r == 3:
                armazenar_em_dicionarios(avaliacoes, discussao, "filme que não gerou discussão nas redes sociais", e)
            if r == 4:
                armazenar_em_dicionarios(avaliacoes, enredo, "enredo mais sem noção", e)

    bocejos = vencedor_simples(dicionario_com_notas(bocejos))
    pausado = vencedor_simples(dicionario_com_notas(pausado))
    revirou = vencedor_simples(dicionario_com_notas(revirou))
    discussao = vencedor_simples(dicionario_com_notas(discussao))
    enredo = vencedor_simples(dicionario_com_notas(enredo))

    todos_filmes = bocejos + pausado + revirou + discussao + enredo
    total = {}
    for u in range(5):
        total[todos_filmes[3 * u]] = todos_filmes.count(todos_filmes[ 3 * u])
    pior = ["nada", 0]
    for i in total:
        if total[i] > pior[1]:
            pior = [i, total[i]]
        if total[i] == pior[1]:
            for o in range(len(todos_filmes)):
                if todos_filmes[o] == i:
                    nota_filme_1 = todos_filmes[o + 1]
                if pior[0] == todos_filmes[o]:
                    nota_filme_2 = todos_filmes[o+1]
            if nota_filme_1 > nota_filme_2:
                pior = [i, total[i]]

    #faz lista com filmes(s) nao avaliados
    filmes_nao_avaliados = []
    for a in range(len(nome_filmes)):
        if not nome_filmes[a] in todas_avaliacoes:
            filmes_nao_avaliados.append(nome_filmes[a]) 

    print("#### abacaxi de ouro ####")
    print()
    print("categorias simples")
    print("categoria: filme que causou mais bocejos")
    print("-", bocejos[0] )
    print("categoria: filme que foi mais pausado")
    print("-", pausado[0])
    print("categoria: filme que mais revirou olhos")
    print("-", revirou[0])
    print("categoria: filme que não gerou discussão nas redes sociais")
    print("-", discussao[0])
    print("categoria: enredo mais sem noção")
    print("-", enredo[0])
    print()
    print("categorias especiais")
    print("prêmio pior filme do ano")
    print("-", pior[0])
    print("prêmio não merecia estar aqui")
    if filmes_nao_avaliados == []:
        print("- sem ganhadores")
    else:
        for a in range(len(filmes_nao_avaliados)):
            if a == 0:
                print("-", filmes_nao_avaliados[a], end= '')
            else:
                print(",", filmes_nao_avaliados[a], end = '')


if __name__ == '__main__':
    main()
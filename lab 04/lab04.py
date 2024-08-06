dias= int(input())

for a in range(dias+1):
    possiveis_brigas = int(input())
    pares_animais = []
    for b in range(possiveis_brigas):
        pares_a= input()
        pares_an = pares_a.split()
        pares_animais = pares_animais + pares_an
    proc = input()
    procedimentos = proc.split()
    quantidade_animais = int(input())
    ind = []
    for c in range(quantidade_animais):
        s = input()
        s1, s2 = s.split()
        ind.append((s1, s2))
    individual = []
    for s1, s2 in ind:
        individual.append(s1)
        individual.append(s2)

    #separa os casais de cachorros que brigam
    brigas = 0
    brigas_impares = []
    brigas_pares= []
    for i in range(0, len(pares_animais)): 
        if i % 2 == 0: 
            brigas_pares.append(pares_animais[i]) 
        else : 
            brigas_impares.append(pares_animais[i]) 

    #separa os procedimentos das quantidades de procedimentos feitos
    procedimentos_tipos = []
    quantidades =[]
    for g in range(0, len(procedimentos)): 
        if g % 2 == 0: 
            procedimentos_tipos.append(procedimentos[g]) 
        else : 
            quantidades.append(procedimentos[g])

    #faz uma lista com a quantidade de procedimentos repetidos
    todos_os_procedimentos = []
    tds = []
    for x in range(0,len(procedimentos_tipos)):
        tds = [procedimentos_tipos[x]] * int(quantidades[x])
        todos_os_procedimentos = todos_os_procedimentos + tds

    #cria listas separadas para os nomes de cada animal e os procedimentos 
    nomes = []
    procedimentos_individuais =[]
    for e in range(0, len(individual)): 
        if e % 2 == 0: 
            nomes.append(individual[e]) 
        else : 
            procedimentos_individuais.append(individual[e]) 

    nomes_atendidos = []
    nomes_nao_atendidos = []
    nomes_procedimento_nao_existe = []

    print("Dia:", a+1)
    for b in range(0,len(brigas_impares)):
        if brigas_pares[b] in nomes and brigas_impares[b] in nomes:
            brigas +=1
    print("Brigas:", brigas)

    for o in range(0, len(nomes)):
        if procedimentos_individuais[o] not in todos_os_procedimentos:
            nomes_procedimento_nao_existe.append(nomes[o])
    for p in range(0,len(nomes)):
        if procedimentos_individuais[p] in todos_os_procedimentos:
            nomes_atendidos.append(nomes[p])
            todos_os_procedimentos.remove(procedimentos_individuais[p])
        elif nomes[p] not in nomes_procedimento_nao_existe:
            nomes_nao_atendidos.append(nomes[p])

    separador = ", "
    if nomes_atendidos != []:
        print("Animais atendidos:", end = '')
        for r in range(len(nomes_atendidos)):
            if r == len(nomes_atendidos):
                print(nomes_atendidos[r])
            else:
                print(nomes_atendidos[r], end=", ")
        print()
    if nomes_nao_atendidos != []:
        print("Animais não atendidos:", end = '')
        for s in range(len(nomes_nao_atendidos)):
            print(nomes_nao_atendidos[s], end=", ")
        print()
    for q in range(0,len(nomes_procedimento_nao_existe)):
        if nomes_procedimento_nao_existe != []:
            print("Animal", nomes_procedimento_nao_existe[q], "solicitou procedimento não disponível.")
    print("")
           


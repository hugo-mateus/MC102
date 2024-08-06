def separa_dna(lista):
    dna = []
    for i in lista:
        for j in i:
                dna.append(j)
    return dna

def numero_inserido_grande(lista, n):
    if n > len(lista):
        n = len(lista) - 1
    return n 
def reverter(lista, i, j):
    i = numero_inserido_grande(lista, i )
    j = numero_inserido_grande (lista, j)
    antes = []
    invertida = []
    depois = []
    for k in range(i):
        antes.append(lista[k])
    for k in range(j, i-1, -1):
        invertida.append(lista[k])
    for k in range(j+1, len(lista)):
        depois.append(lista[k])
    return antes + invertida + depois

def transpor(lista, i, j, k):
    i = numero_inserido_grande(lista,i)
    j= numero_inserido_grande(lista,j)
    k = numero_inserido_grande(lista,k)
    antes_transpor  =[]
    nova_primeira = []
    nova_segunda = []
    depois_transpor = []
    for e in range(i):
        antes_transpor.append(lista[0])
        lista.remove(lista[0])
    for f in range(j-i+1):
        nova_segunda.append(lista[0])
        lista.remove(lista[0])
    for h in range(k-j):
        nova_primeira.append(lista[0])
        lista.remove(lista[0])
    for g in range(len(lista)):
        depois_transpor.append(lista[0])
        lista.remove(lista[0])
    return antes_transpor + nova_primeira +nova_segunda +depois_transpor

def combinar(lista, lista_1, i):
    i = numero_inserido_grande(lista,i)
    antes_combinar = []
    depois_combinar =[]
    for i in range(i):
        antes_combinar.append(lista[0])
        lista.remove(lista[0])
    for n in range(len(lista)):
        depois_combinar.append(lista[0])
        lista.remove(lista[0])
    return antes_combinar + lista_1 +depois_combinar

def concatenar(lista, lista_1):
    return lista+lista_1

def remover(lista, i, j ):
    i = numero_inserido_grande(lista,i)
    j = numero_inserido_grande(lista,j)
    primeira_remover  = []
    for n in range(i):
        primeira_remover.append(lista[0])
        lista.remove(lista[0])
    for n in range(j-i+1):
        lista.remove(lista[0])
    return primeira_remover+lista

def transpor_e_reverter(lista, i , j , k):
    i = numero_inserido_grande(lista,i)
    j = numero_inserido_grande(lista,j)
    k = numero_inserido_grande(lista,k)
    transposta= transpor(lista, i, j, k)
    return reverter(transposta, i, k)

def buscar(lista_1, lista_2):
    conta = 0
    n = len(lista_2)
    for i in range(len(lista_1) - n + 1):
        if lista_1[i:i+n] == lista_2:
            conta += 1
    return conta

def buscar_bidirecional(lista_1, lista_2):
    conta= buscar(lista_1, lista_2)
    lista_invertida = reverter(lista_2, 0 , len(lista_2)-1)
    conta = conta + buscar(lista_1, lista_invertida)
    return conta

dna__ = input()
dna_ = dna__.split()
dna = separa_dna(dna_)
comando = 0

while comando != "sair":
    inputs_ = input()
    inputs = inputs_.split()
    comando = inputs[0]
    if comando == "reverter":
        dna = reverter(dna, int(inputs[1]), int(inputs[2]))
    
    if comando == "transpor":
        dna = transpor(dna, int(inputs[1]), int(inputs[2]), int(inputs[3]))

    if comando == "combinar":
        lista = inputs[1]
        dna_para_modificar = separa_dna(lista)
        dna = combinar(dna, dna_para_modificar, int(inputs[2]))

    if comando == "concatenar":
        lista = inputs[1]
        dna_para_modificar = separa_dna(lista)
        dna = concatenar(dna,dna_para_modificar)
    
    if comando == "remover":
        dna = remover(dna, int(inputs[1]), int(inputs[2]))

    if comando == "transpor_e_reverter":
        dna = transpor_e_reverter(dna, int(inputs[1]), int(inputs[2]), int(inputs[3]))

    if comando == "buscar":
        lista = inputs[1]
        dna_para_modificar = separa_dna(lista)
        print(buscar(dna, dna_para_modificar))
    
    if comando == "buscar_bidirecional":
        lista = inputs[1]
        dna_para_modificar = separa_dna(lista)
        print(buscar_bidirecional(dna, dna_para_modificar))
    
    if comando == "mostrar":
        dna_para_mostrar = ''.join(dna)
        print(dna_para_mostrar)
from math import fabs


def dano_de_manhattan(ataques, x, especificos, partes, u):
    """calcula a distancia de manhattan"""
    return int(especificos[u-1][2]) - ( fabs(int(partes[x][3]) - int(ataques[3])) + fabs(int(partes[x][4]) - int(ataques[4]))) 

def ataque_contra_aloy(u, especificos, pv_aloy):
    """"calcula o dado da aloy apos um ataque"""
    for y in range(u):
        pv_aloy -= int(especificos[u-1][1]) 
    return pv_aloy


def tao_mortos(especificos):
    """determina se todas as máquinas estão mortas"""
    tao_mortos = True
    for i in range(len(especificos)):
        if int(especificos[i][0]) > 0.0:
            tao_mortos = False
    return tao_mortos

def ataque_da_aloy(ataques, partes, especificos, u):
    """calcula o dano que a aloy causa e atualiza a vida das máquinas"""
    for i in range(len(partes)):
        if ataques[1] == partes[i][0]:
            break
    if partes[i][3:5] != ataques[3:5] and (partes[i][1] != "todas" and partes[i][1] != ataques[2]):
        # se as fraquezas e os pontos críticos e atingidos forem diferentes
        dano = (int(partes[i][2]) - dano_de_manhattan(ataques, i, especificos, partes, u)) / 2
    elif partes[i][3:5] != ataques[3:5]:
        #se somente os pontos críticos e atingidos forem diferentes
        dano = int(partes[i][2]) - dano_de_manhattan(ataques, i, especificos, partes, u)
    elif partes[i][1] != "todas" or partes[i][1] != ataques[2]:
        #se as fraquezas da flecha e da parte forem diferentes
        dano = int(partes[i][2]) / 2
    else: 
        dano = int(partes[i][2])
    especificos[u-1][0] = int(especificos[u-1][0]) - fabs(dano)
    return especificos[u-1][0]


def recupera_vida(pv_aloy, pv_maximo_aloy):
    """"recupera a vida de aloy após o final de um combate"""
    pv_aloy += pv_maximo_aloy * 0.5
    if pv_aloy > pv_maximo_aloy:
        pv_aloy = pv_maximo_aloy
    return pv_aloy


def flechas_utilizadas(ataques, flechas_faltando, flechas_usadas, flechas):
    """atualiza quais flechas a aloy usou, e determina se ela não está mais com felchas sobrando"""
    global acabou_as_flechas
    acabou_as_flechas = False
    if ataques[2] in flechas:
        if ataques[2] not in flechas_faltando:
            flechas_faltando[ataques[2]] = int(flechas[ataques[2]]) - 1
        else:
            flechas_faltando[ataques[2]] = int(flechas_faltando[ataques[2]]) -1
        if flechas_faltando[ataques[2]] <= 0:
            acabou_as_flechas = True
            return acabou_as_flechas
    if ataques[2] in flechas_usadas:
        flechas_usadas[ataques[2]] = int(flechas_usadas[ataques[2]]) + 1
    else:
        flechas_usadas[ataques[2]] = 1


def ataques_criticos(partes, ataques, criticos):
    """atualiza o diconário com a posição e quantidade de ataques críticos feitos"""
    for i in range(len(partes)):
        if ataques[1] == partes[i][0]:
            break
    if partes[i][3:5] == ataques[3:5]:
        t = int(ataques[3]), int(ataques[4])
        if ataques[3] in criticos and ataques[4] in criticos:
            criticos[t] = int(criticos[t]) + 1
        else:
            criticos[t] = 1
    return criticos


def main():
    pv_aloy = int(input())
    pv_maximo_aloy = pv_aloy
    flechas_ = input().split()
    flechas = {}
    for i in range(len(flechas_) // 2):
        flechas[flechas_[0 + (2 * i)]] = flechas_[1+ (2 * i)]
    n = int(input())
    u = int(input())
    especificos = []
    r = 0
    flechas_usadas = {}
    criticos = {}
    acabou_as_flechas = False
    while r < n and pv_aloy > 0:
        flechas_faltando = flechas.copy()
        for p in range(u):
            pv_aloy_comeco = pv_aloy
            especificos_ = input().split()
            especificos.append(especificos_)
            partes = []
            for w in range(int(especificos[r][2])):
                partes_ = input().split(", ")
                partes.append(partes_)
            quantidade_ataque = 0
            while (not tao_mortos(especificos)) and (pv_aloy > 0): 
                quantidade_ataque += 1
                ataques = input().split(", ")
                ataque_da_aloy(ataques, partes, especificos, u)
                flechas_utilizadas(ataques, flechas_faltando, flechas_usadas, flechas)
                ataques_criticos(partes, ataques, criticos)
                if quantidade_ataque % 3 == 0:
                    ataque_contra_aloy(u, especificos, pv_aloy) 
                if acabou_as_flechas:
                    break
        print("Combate", u-1, end = '')
        print(", vida =", pv_aloy_comeco)
        print("Máquina", n-1, end = ' ')
        print("derrotada")
        print("Vida após o combate =", pv_aloy)
        print("Flechas utilizadas:")
        for x in flechas_usadas:
            print("-", x, end =': ')
            print(flechas_usadas[x], "/", sep = "", end = '')
            print(flechas[x] )
        if criticos != {}:
            print("Críticos acertados:")
            for o in range(u):
                print("Máquina ", n+u-2, ":", sep ="")
                for c in criticos:
                    print("- ", c, ":", sep = "",end=' ')
                    print(criticos[c], "x", sep = "")
        if acabou_as_flechas:
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
        elif pv_aloy > 0:
            print("Aloy provou seu valor e voltou para sua tribo.")
        else:
            print("Aloy foi derrotada em combate e não retornará a tribo.")
        pv_aloy = recupera_vida(pv_aloy, pv_maximo_aloy)
        print() 
        r += 1 


if __name__ == '__main__':
    main()
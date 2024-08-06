J = int(input())

n = input()
numeros = n.split()

inter = input()
intervalo = inter.split()

#separa a lista dos intervalos entre os limites inferiores e superiores
impares = []
pares= []
for i in range(0, len(intervalo)): 
    if i % 2 == 0: 
        pares.append(intervalo[i]) 
    else : 
        impares.append(intervalo[i]) 

#subtrai os limites
subtraido = []
for i in range(0, len(impares)):
    sub = int(impares[i]) - int(pares[i])
    subtraido.append(sub)

#encontra quantos jogadores estarão no primeiro grupo
if J % 2 == 0:
    jogadores_primeiro = int(J/2)
else:
    jogadores_primeiro = int((J // 2) + 1)

#calcula as pontuações nos dois grupos
multiplicado = []
for i in range(0, jogadores_primeiro):
    m  = int(subtraido[i]) * int(numeros[i])
    multiplicado.append(m)

soma = []
for i in range(jogadores_primeiro, len(numeros)):
    s = int(subtraido[i]) + int(numeros[i])
    soma.append(s)

pontuacao = multiplicado + soma

#encontra vencedor
i=0
vencedor_pontos = 0
posicao_vencedor = 0
empate = False
while i < J:
    if int(pontuacao[i]) == vencedor_pontos and vencedor_pontos != 0:
        empate = True
    if int(pontuacao[i]) > vencedor_pontos:
        vencedor_pontos = int(pontuacao[i])
        posicao_vencedor = i + 1
    i += 1 

if empate == True:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print("O jogador número", posicao_vencedor, end='')
    print(" vai receber o melhor bolo da cidade pois venceu com", vencedor_pontos, end ='')
    print(" ponto(s)!")





    



  







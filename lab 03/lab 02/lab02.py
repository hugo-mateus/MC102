print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda ", end='')
print("a algumas poucas perguntas para ter uma recomendação.")

p_1 = int(input("Seu SO anterior era Linux?\n(0) Não\n(1) Sim\n"))

if p_1 == 0:
    p_2 = int(input ("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n"))
    if p_2 != 0 and p_2 != 1:
        print("Opção inválida, recomece o questionário.")
    if p_2 == 0 or p_2 == 1:
        print("Você passará pelo caminho daqueles que decidiram abandonar sua ", end='')
        print("zona de conforto, as distribuições recomendadas são: ", end='')
    if p_2 == 0:
        print("Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
    elif p_2 == 1:
        print ("ElementaryOS, ApricityOS.")

elif p_1 == 1:
    p_3 = int(input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n"))
    if p_3 != 0 and p_3 != 1 and p_3 != 2:
        print("Opção inválida, recomece o questionário.")
    if p_3 == 0 or p_3 == 2:
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, " , end = '')
        print("as distribuições que servirão de base para seu aprendizado são: ", end = '')
    if p_3 == 0:
        print("Ubuntu Mint, Fedora.")
    if p_3 == 2:
        print("Kali Linux, Black Arch.")
    if p_3 == 1:
        p_4 = int(input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n"))
        if p_4 != 0 and p_4 != 1:
            print("Opção inválida, recomece o questionário.")
        if p_4 == 0:
            p_5 = int(input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n"))
            if p_5 != 0 and p_5 != 1:
                print("Opção inválida, recomece o questionário.")
            if p_5 == 0:
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, " , end= '')
                print("as distribuições que servirão de base para seu aprendizado são: ", end = '')
                print("Antergos, Arch Linux.")
            if  p_5 == 1:
                print("Suas escolhas te levaram a um caminho repleto de desafios, ", end = '') 
                print("para você recomendamos as distribuições: ", end = '')
                print("Gentoo, CentOS, Slackware.")
        elif p_4 == 1:
            p_6 = int(input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n"))
            if p_6 != 0 and p_6 != 1:
                print("Opção inválida, recomece o questionário.")
            if p_6  == 0:
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, " , end= '')
                print("as distribuições que servirão de base para seu aprendizado são: ", end = '')
                print("OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
            elif p_6 == 1:
                print("Suas escolhas te levaram a um caminho repleto de desafios, ", end = '') 
                print("para você recomendamos as distribuições: ", end = '')
                print("Manjaro, ApricityOS.")
        
if p_1 != 0 and p_1 != 1:
    print("Opção inválida, recomece o questionário.")
def imprime_cruz(matriz): # Imprime aquela cruz do jogo da velha, com indíces
    print("  C1   C2   C3")
    for i in range(3):
        print(f"L{i + 1} ", end="")
        for j in range(3):
            print(matriz[i][j], end="")
            if j < 2:
                print("  |  ", end="")
        print()
        if i < 2:
            print("-" * 18)

def pedePosicaoUser(matriz, refaz): # Pede posição para o jogador, recebe a matriz e se está refazendo a pergunta
    if refaz:   # Se a jogada foi inválida, refaz a pergunta
        print(" ")
        print("vvvvvvvv Posição errada! vvvvvvvvv")
        print("Linhas de 1 a 3 e Colunas de 1 a 3")
        print("Verifique se a posição está certa!")
        print(" ")
        imprime_cruz(matriz)
        print(" ")
    
        linha = int(input("Qual a linha:"))
        coluna = int(input("Qual a coluna:"))
        preenche(linha, coluna, matriz) 

    else:  
        print("Sua vez, observe o jogo abaixo e escolha a linha e depois a coluna: ")
        print(" ")
        imprime_cruz(matriz)
        print(" ")
    
        linha = int(input("Qual a linha:"))
        coluna = int(input("Qual a coluna:"))
        preenche(linha, coluna, matriz)

def preenche(linha, coluna, matriz): # função que altera a matriz do jogo
    
    l = linha - 1 # Traduz a entrada da interface, pro usuario não ter que por linha 0 ou coluna 0
    c = coluna - 1

    if (l >= 0 and l <= 2) and (c >= 0 and c <= 2): # Trata se o indice é válido
        if matriz[l][c] == " ": # Trata se o campo está limpo
            matriz[l][c] = "x"
            imprime_cruz(matriz)
            print(" ")
        else:
            pedePosicaoUser(matriz, True)
    else: 
        pedePosicaoUser(matriz, True)

def ProcuraVitoria(x_ou_bola, matriz): # Percorre a matriz como "x" ou "o" e verifica se alguém ganhou

    def contaC(c): # retorna vitória se tem 3 * "x" ou "o" na mesma linha
        if c == 3:
            return True
        else:
            return False

    c = 0

    # Percorre linhas ---
    for i in range(3):
        c = 0
        for j in range(3): 
            if matriz[i][j] == x_ou_bola:
                c = c + 1 # Conta quantos "x" ou "o" tem na linha percorrida
        if contaC(c):
            return True

    # Percorre coluna |
    for j in range(3):
        c = 0
        for i in range(3):
            if matriz[i][j] == x_ou_bola:
                c = c + 1 # Conta quantos "x" ou "o" tem na coluna percorrida
        if contaC(c):
            return True

    # Percorre diagonal X
    if matriz[1][1] == x_ou_bola:
        if matriz[0][0] == x_ou_bola and matriz[2][2] == x_ou_bola: #se for vencer assim: \
            return True
        if matriz[2][0] == x_ou_bola and matriz[0][2] == x_ou_bola: #se for vencer assim: /
            return True

    return False

def ProcuraEmpate(matriz): # Ver se tem espaços vazios, caso tenha não decreta empate
    for i in matriz:
        for j in i:
            if j == " ":
                return False
    return True

# --------Toda a dor de cabeça e lógica esta centralizada aqui! algoritmo MiniMax()-------- #

# Contextualizando: é responsável por calcular a utilidade de um determinado estado do jogo para um jogador, 
# levando em consideração todas as jogadas possíveis até o final do jogo, por busca exata. O valor retornado pelo minimax é 
# usado para determinar qual é a melhor jogada para um jogador em um determinado estado do jogo. A função 
# é chamada recursivamente para explorar todas as possibilidades de jogadas e encontrar a melhor estratégia 
# para o jogador atual.

# Explicação mais simples: Imagine que ele se dê ao trabalho de ficar marcando "o" em todos os quadrinhos um de cada vez, 
# e depois faça a mesma coisa só que marcando o "x" como se fosse o adversário, ou melhor como se fosse o personagem Chaves 
# no episódio que ele vende churros para ele mesmo, tecnicamente isso é chamado de recursão, assim ele simula do começo ao 
# resultado de cada jogada e ao final de tudo retorna a melhor jogada, ou seja a que ele vence ou empata, ou melhor dizendo 
# ele dá um pontinho para cada umas das situações e se a pontuaçao for a mais alta é a melhor jogada calculada.

# Recebe a matriz, a profundidade para a arvore, e se está atacando ou defendendo (boolean is_max)
def minimax(matriz, profundidade, is_max): 
    
    #___________________________________
    if ProcuraVitoria("o", matriz):     #|
        return 1                        #|
    if ProcuraVitoria("x", matriz):     #| - Retorna valores caso vitória (1), derrota(-1) e empate(0)
        return -1                       #|
    if ProcuraEmpate(matriz):           #|
        return 0                        #|
    #____________________________________|
    
    if is_max: # Se tiver simulando ataque da IA
        praGanhar = -float('inf') #Jogando praGanhar ela recebe o negativo infinito, qualquer valor maior que o algoritmo
                                  # encontrar será maior que ele.  
        for i in range(3):
            for j in range(3):          
                if matriz[i][j] == " ":
                    matriz[i][j] = "o"  # Aqui ele começa a simulação, pega o primeiro espaço vazio e ver se é uma boa jogada
                    recursaoRefaz = minimax(matriz, profundidade + 1, False) # Chama a recursão, e vai aprofudando e ja joga
                                                                             # o algoritmo para simular a jogada do adversário, passando o False.
                    matriz[i][j] = " " # Apaga a alteração, para manter a integridade da matriz
                    praGanhar = max(praGanhar, recursaoRefaz) # Compara e caso encontre uma de maior pontuação ele muda o valor
        return praGanhar 
    else: # Se tiver simulando ataque do adversario
        praPerder = float('inf') # Começa com o infinito positivo, assim qualquer valor menor que o algoritmo encontrar, será menor que ele
        for i in range(3):
            for j in range(3):
                if matriz[i][j] == " ":
                    matriz[i][j] = "x" # Simula a jogada do adversário
                    recursaoRefaz = minimax(matriz, profundidade + 1, True) # Chama a recursão e procura de novo o valor, já passando True pra dar a vez
                                                                            # de simular a jogada da IA
                    matriz[i][j] = " "
                    praPerder = min(praPerder, recursaoRefaz) # Compara e caso encontre uma menor ele já recebe esse valor
        return praPerder

def melhor_jogada(matriz): #Pega a melhor jogada
    melhor_jogo = None #jogada
    melhor_ponto = -float('inf') #começa com o negativo infinito, assim qualquer valor é maior que isso

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == " ":
                matriz[i][j] = "o"
                recursoRefaz = minimax(matriz, 0, False) #Chama a função minimax(passa a matriz, profundidade 0 pro inicio, e passa a vez para a IA atacar)
                matriz[i][j] = " "

                if recursoRefaz > melhor_ponto: # Toda vez que simula a jogada em um campo limpo e recebe um valor, caso ela tenha uma pontuação maior, ou seja
                                                # é uma jogada melhor, a pontuação é salva na linha abaixo:
                    melhor_ponto = recursoRefaz
                    melhor_jogo = (i, j)        # e melhor_jogo recebe essa jogada

    return melhor_jogo # Ao final de todas as verificações, vai retornar a melhor jogada possível

#| ------------------------------------- MiniMax()---------------------------------------- |#


def pedePosicaoIA(matriz): # Pede posição da IA e depois chamam as funções que "Pensam"
    print("A IA está jogando!!")

    jogo = melhor_jogada(matriz)

    linha, coluna = jogo

    preencheIA(linha, coluna, matriz) # Chama função que preenche a matriz

def preencheIA(linha, coluna, matriz): # Função que preenche a matriz
    l = linha
    c = coluna

    matriz[l][c] = "o"

    imprime_cruz(matriz)

    print("   ")
    print("   ")



# main
contador = 0 #vai ser responsável por contar a vez
matriz_velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] 

while True:
    contador = contador + 1

    if contador % 2 == 1:  # É a vez do jogador (ímpar)
        pedePosicaoUser(matriz_velha, False)
    else:  # É a vez da IA (par)
        pedePosicaoIA(matriz_velha)

#---------------------------------------------
    if ProcuraVitoria("o", matriz_velha):
        imprime_cruz(matriz_velha)
        print("A IA (o) venceu!")
        break
    elif ProcuraVitoria("x", matriz_velha):
        imprime_cruz(matriz_velha)              # chamas as funções em todas as repetiçoes e fica procurando vitórias ou empates
        print("Você (x) venceu!")               #
        break
    elif contador == 9:
        imprime_cruz(matriz_velha)
        print("Empate!")
        break
#---------------------------------------------
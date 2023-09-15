# JogoDaVelha_IA

Jogo da velha com inteligência artificial que pensa na melhor jogada toda vez que é sua vez de jogar, 
por meio da busca exata implementada no algoritmo minimax que simula a jogada até o seu possível fim e pontue como maior (caso for ganhar) ou menor valor (caso for perder), 
escolhendo sempre a de maior valor para fazer a sua jogada.

O algoritmo Minimax:

ROTINA minimax(nó, profundidade, maximizador)
    SE nó é um nó terminal OU profundidade = 0 ENTÃO
        RETORNE o valor da heurística do nó
    SENÃO SE maximizador é FALSE ENTÃO
        α ← +∞
        PARA CADA filho DE nó
            α ← min(α, minimax(filho, profundidade-1,true))
        FIM PARA
        RETORNE α
    SENÃO
        //Maximizador
        α ← -∞
        //Escolher a maior dentre as perdas causadas pelo minimizador
        PARA CADA filho DE nó
            α ← max(α, minimax(filho, profundidade-1,false))
        FIM PARA
        RETORNE α
    FIM SE
FIM ROTINA

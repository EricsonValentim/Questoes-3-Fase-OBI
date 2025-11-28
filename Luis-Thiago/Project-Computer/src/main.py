def executar_instrucoes(tamanho_memoria, lista_instrucoes):
   
    # Inicializa a memória com zeros (índices de 1 a N)
    memoria = [0] * (tamanho_memoria + 1)

    # Processa cada instrução da lista
    for instrucao in lista_instrucoes:

        tipo_de_instrucao = instrucao[0]

        # INSTRUÇÃO FRENTE (1 i V)
        if tipo_de_instrucao == 1:  
            posicao_inicial = instrucao[1]
            valor_inicial = instrucao[2]

            valor_atual = valor_inicial
            posicao_atual = posicao_inicial

            while posicao_atual <= tamanho_memoria and valor_atual > 0:
                memoria[posicao_atual] += valor_atual
                valor_atual -= 1
                posicao_atual += 1

        # INSTRUÇÃO TRÁS (2 i V)
        elif tipo_de_instrucao == 2:
            posicao_inicial = instrucao[1]
            valor_inicial = instrucao[2]

            valor_atual = valor_inicial
            posicao_atual = posicao_inicial

            while posicao_atual >= 1 and valor_atual > 0:
                memoria[posicao_atual] += valor_atual
                valor_atual -= 1
                posicao_atual -= 1

        # INSTRUÇÃO IMPRIME (3 i)
        elif tipo_de_instrucao == 3:
            posicao_solicitada = instrucao[1]
            print(memoria[posicao_solicitada])


# Execurução do código com exemplo de entrada
tamanho_memoria = 16
lista_instrucoes = [
    (1, 4, 8),   # FRENTE 4º = 8
    (2, 16, 3),  # TRÁS 16º = 3
    (2, 2, 12),  # TRÁS 2º = 12
    (1, 8, 7),   # FRENTE 8º = 7
    (3, 4),      # IMPRIME SLOT 4º
    (3, 14),     # IMPRIME SLOT 14º
    (3, 1)       # IMPRIME SLOT 1º
]

executar_instrucoes(tamanho_memoria, lista_instrucoes)
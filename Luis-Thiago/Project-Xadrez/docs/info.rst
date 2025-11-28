* Explicação do Algoritmo
#N, T = map(int, input().split())
- Lê uma linha do teclado.
  Divide ela em duas partes (antes e depois do espaço).
  Converte essas duas partes para inteiros.
  Guarda o primeiro número em N e o segundo em T.

#if T == 0:
- Verifica se T é igual a zero.
  
#resultado = N
- Se não há torres, o rei pode ocupar qualquer das N casas.
  Salva esse valor em resultado.

#elif T == 1:
- Se não caiu no if, testa agora se há 1 torre.

#resultado = N * (N - 1)
- Calcula todas as maneiras possíveis de colocar 1 rei e 1 torre em posições diferentes.

#else:
- Se não é 0 nem 1 torre, significa que T == 2.

#resultado = (N - 2) * (N - 1) * N // 6
- Calcula o número de posições possíveis onde:
 existem duas torres,
 o rei fica entre elas.
 Esse cálculo usa a fórmula de combinações.

 #print(resultado)
 - Mostra o número final calculado na tela.
- Uma seção mais detalhada:

Explicação em Português estruturado;
- Pseudocódigo:
  
- algoritmo "xadrez_variantes"

var
    N, T, resultado: inteiro

inicio

    leia(N, T)

    se (T = 0) entao
        resultado <- N

    senao
        se (T = 1) entao
            resultado <- N * (N - 1)
        senao
            resultado <- (N - 2) * (N - 1) * N / 6
        fimse
    fimse

    escreva(resultado)

fimalgoritmo

"""
# executar instruções ler e calcular as possibilidades das torres e do rei no tabuleiro de xadrez.
tipo de instrução;
algoritmo Xadrez
    leia(indicador de posição, numeros de torres)
    calcular_combinacoes(indicador de posição, numeros de torres) -> resultado 
"""
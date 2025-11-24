'''
============ Questão OBI 2017 nível Sênior, fase 2 ====================== 

                            DARIO E XERXES

Dario e Xerxes são dois amigos que bricam de pedra papel e tesoura
logo, eles, antes disso, dão para realizar com 5 opções e não 3,
com N sendo impar e quantia de rodadas. Se Dario escolher 0
e Xerxes 3, logo Xerxes é o vencedor da rodada e assim por dainte.  
vencedor da rodada.

======= Entrada ===========================================================
A primeira linha da entrada contém um inteiro N, o número de rodadas na partida. Cada uma das N linhas seguintes contém dois inteiros D e X, representando a mão que os jogadores dario e xerxes, respectivamente, jogaram em uma rodada.

====== Saída
Seu programa deve imprimir uma linha contendo o nome do jogador que venceu a partida: dario ou xerxes. Todas as letras devem ser minúsculas, sem nenhum acento!
===== restrições ============================================================
    * 1 ≤ N ≤ 999, N é impar
    * 0 ≤ D,X ≤ 4 e D ≠ Xcv
=============================================================================
Exemplos
------Entrada-------
    3
    1 3
    4 2
    0 2
-----Saída----------
    dario

-----Entrada--------
    1
    3 1
-----Saída----------
    xerxes	
'''

# Cria uma função principal
def main():
# Contador para a vitória de Dario
    dario = 0
# Lê o número de rodadas
    N = int(input())
# Para cada rodada
    for _ in range(N):
# Lê a rodada de Dario (D) e de Xerxes (X)
       D,X = map(int, input().split())
       if X == (D + 1) % 5 or X == (D + 2) % 5:
 # Contabiliza vitória de Dairo         
            dario = dario + 1 
# Após todas as rodadas verifica quem venceu mais
    if dario > N / 2:
        print("dairo")
    else:
        print("xerxes")
main()




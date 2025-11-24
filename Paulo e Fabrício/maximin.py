'''
============ Questão OBI 2018 nível Sênior, fase 3 ======================
                             
                             MAXIMIN
                             
*************************************************************************
Maximin é uma pessoa muito pessimista, ele prefere esperar pelo resultado
que menos importar, o desfavoravél. Ele e seus amigos desenvolveram um 
jogo em que todos possuem números sorteados N escritos em papel e escolhem
ao mesmo tempo um limite inferiro L e um limite superior R, para servir de 
parâmetro aos numeros sorteados e postos dentro de um caixa, todos os 
númemros sendo inteiros. A estratégia de Maximin então é escolher 
o número que tem a maior das menores diferenças.

*************************************************************************
==== Entrada =============================================================
A primeira linha contém três inteiros N, L e R representando respectivamente, a quantidade de participantes (incluindo Maximin), o menor e o maior número que pode ser escolhido na rodada. A linha seguinte contém N inteiros ai representando os números escritos nos papéis.

===== Saída ==============================================================

Seu programa deve produzir uma única linha, contendo um inteiro, a pontuação esperada por Maximin.

===== Restrições =========================================================

    2 ≤ N ≤ 105
    -109 ≤ L ≤ R ≤ 109
    -109 ≤ ai ≤ 109

===== Informações sobre a pontuação ======================================

    Para um conjunto de casos de testes valendo 20 pontos:
    2 ≤ N ≤ 102
    -1000 ≤ L ≤ R ≤ 1000
    -1000 ≤ ai ≤ 1000
    Para um conjunto de casos de testes valendo 30 pontos:
    2 ≤ N ≤ 104
    -105 ≤ L ≤ R ≤ 105
    -105 ≤ ai ≤ 105

Exemplos
-----Entrada-------
    3 7 37
    10 17 28
-----Saída---------
        9
-----Entrada-------
    5 -6 6
    8 -4 -3 6 12
-----Saída---------
       4      
=============================================================================
'''
# Cria a função principal
def main():
# Atribuição de variáveis
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    for i in range(1, n):
        a = arr[i - 1]
        b = arr[i]
        meio = (a + b) // 2
        if l <= meio <= r:
            res = max(res, min(b - meio, meio - a))
        elif meio < l < b:
            res = max(res, b - l)
        elif a < r < meio:
            res = max(res, r - a)
    if r > arr[-1]:
        res = max(res, r - arr[-1])
    if l < arr[0]:
        res = max(res, arr[0] - l)
    print(res)
main()
 
 
 
 
 
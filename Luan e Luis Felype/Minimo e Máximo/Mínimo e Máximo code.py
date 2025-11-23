def soma_digitos(n):
    return sum(int(d) for d in str(n))
# (1) ^^^^^^
S = int(input().strip())
A = int(input().strip())
B = int(input().strip())
# (2) ^^^^^^
menor = None
maior = None
# (3) ^^^^^^
for num in range(A, B + 1):
    if soma_digitos(num) == S:
        if menor is None:
            menor = num
        maior = num
# (4) ^^^^^^
print(menor)
print(maior)

# RESOLUÇÃO E EXPLICAÇÃO DO CÓDIGO
# //
# O enunciado pede um programa que calcule a resposta de uma forma mais rapida para o desafio do pedrinho;
# Primeiro criamos uma função para calcular a soma dos digitos (1);
# A função recebe um numero 'n', se n = 123 então str(n) se torna "123";
# "int(d) for d in str(n)" cria uma sequencia de digitos convertidos para números;
# 'sum' soma todos os elementos gerados;
# Depois o programa lê os valores digitados pelo usuario com S = int(input().strip()), A e B; (2)
# S > sendo a soma desejada, A > inicio do intervalo, B > fim do intervalo;
# Menor e maior = none, porque não tem valor ainda, usamos para detectar quando encontramos o primeiro numero valido para o menor; (3)
# "range(A, B + 1)" começa em A e vai até B, B + 1 para ir antes do ultimo valor, A = 10 e B = 12 > 10, 11, 12;(4)
# if soma_digitos, para chamar a função e comparar com S, se igual então válido:(4)
# Como menor começa com none, o primeiro numero encontrado será o menor; (4)
# maior = num, não tem condição pois a cada novo número válido encontrado, ele será maior que os anteriores;(4)
# No final do loop, 'maior' será realmente o maior número cuja soma dos dígitos é S;
# a questão pede duas linhas na saida então printamos o resultado, prints.

# //

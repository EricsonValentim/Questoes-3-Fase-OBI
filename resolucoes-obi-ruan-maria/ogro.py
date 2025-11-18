#  Ogro

# O Ogro da Nlogônia está aprendendo a contar até dez usando os dedos das mãos (assim como os humanos, ele possui 2 mãos com 5 dedos cada). 

# Ele está treinando muito, mas gostaria de ter um aplicativo para ajudá-lo nessa empreitada. O Ogro aprendeu a mostrar a representação de um número com as mãos da seguinte forma:

# Se o número pode ser representado usando apenas uma das mãos, o Ogro usa os dedos na mão esquerda e mantém a mão direita fechada.Caso contrário, o Ogro mostra todos os cinco dedos da mão esquerda, e na mão direita mostra os dedos que faltam para representar o número.

# Sua tarefa é ajudar o Ogro em seu treinamento, escrevendo um programa para, dado um número entre 0 e 10, mostrar a configuração de dedos correspondente a esse número, de acordo com as regras acima.

N = int(input())

# mão esquerda
if N == 0:
    esquerda = "*"
elif N <= 5:
    esquerda = "I" * N
else:
    esquerda = "IIIII"

# mão direita
if N <= 5:
    direita = "*"
else:
    direita = "I" * (N - 5)

print(esquerda)
print(direita)


# Resolução da Questão nivel sênior muro da 3ª fase da OBI2018
# Autores: Renan Cardoso e Carlos Eduardo

MOD = 1_000_000_007

N = int(input())

if N == 0:
    print(1)
    exit()
elif N == 1:
    print(1)
    exit()
elif N == 2:
    print(5)
    exit()

a, b, c = 1, 1, 5

for _ in range(3, N + 1):
    a, b, c = b, c, (c + 4*b + 2*a) % MOD

print(c)
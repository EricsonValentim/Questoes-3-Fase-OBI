N, T = map(int, input().split())

if T == 0:
    # Apenas o rei: pode estar em qualquer das N casas
    resultado = N

elif T == 1:
    # 1 torre + 1 rei: escolher posições distintas
    resultado = N * (N - 1)

else:  # T == 2
    # Rei deve estar entre as duas torres
    # Fórmula que conta todas as combinações possíveis:
    resultado = (N - 2) * (N - 1) * N // 6

print(resultado)

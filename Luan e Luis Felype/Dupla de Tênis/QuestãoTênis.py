# Leitura dos quatro inteiros.
A = int(input("Nível do jogador A: ").strip())
B = int(input("Nível do jogador B: ").strip())
C = int(input("Nível do jogador C: ").strip())
D = int(input("Nível do jogador D: ").strip())

# Calcular as diferenças absolutas das 3 partições possíveis.
dif1 = abs((A + B) - (C + D))  # (A,B) vs (C,D)
dif2 = abs((A + C) - (B + D))  # (A,C) vs (B,D)
dif3 = abs((A + D) - (B + C))  # (A,D) vs (B,C)

# A resposta é a menor das três variáveis.
print(min(dif1, dif2, dif3))

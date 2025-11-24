print("Insira os níveis de cada jogador (A, B, C e D):")

A = int(input("Nível do jogador A: "))
B = int(input("Nível do jogador B: "))
C = int(input("Nível do jogador C: "))
D = int(input("Nível do jogador D: "))

# Calculando as três combinações possíveis
comb1 = abs((A + B) - (C + D))  # Duplas: (A,B) e (C,D)
comb2 = abs((A + C) - (B + D))  # Duplas: (A,C) e (B,D)
comb3 = abs((A + D) - (B + C))  # Duplas: (A,D) e (B,C)

# Descobrindo a menor diferença
menor_dif = min(comb1, comb2, comb3)

# Descobrindo qual combinação gerou a menor diferença
if menor_dif == comb1:
    escolhida = f"Duplas escolhidas: (A, B) e (C, D)"
elif menor_dif == comb2:
    escolhida = f"Duplas escolhidas: (A, C) e (B, D)"
else:
    escolhida = f"Duplas escolhidas: (A, D) e (B, C)"

# Exibindo o resultado final
print("\n----------------------------------")
print("Menor diferença possível:", menor_dif)
print(escolhida)
print("----------------------------------")

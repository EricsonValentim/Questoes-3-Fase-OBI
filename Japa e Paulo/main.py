# Jogo do Preto e Branco
# Uma peça branca não pode estar do lado de outra branca
# Deve haver uma preta ao lado de uma branca
# Linhas e Colunas não podem exceder 6
# Pretas não podem exceder 10

matrizTabuleiro = []

def verificacao(entrada, campo, max, min) -> int:
    if entrada == "":
        print("Você precisa digitar alguma coisa!")
        return 1
    if not entrada.isdigit():
        print("⚠️ Digite apenas números.")
        return 1
    val = int(entrada)
    if val >= max:
        print(f"O número de {campo} não pode exceder {max - 1}! Tente novamente!")
        return 1
    if val <= min:
        print(f"O número de {campo} não pode ser menor do que {min + 1}! Tente novamente!")
        return 1
    return 0

def inputLinha():
    while True:
        entrada = input("Digite o número de linhas: ").strip()
        if verificacao(entrada, "linha", 6, 1) == 1:
            continue
        return int(entrada)

def inputColuna():
    while True:
        entrada = input("Digite o número de colunas: ").strip()
        if verificacao(entrada, "coluna", 6, 1) == 1:
            continue
        return int(entrada)

def inputPretas():
    while True:
        entrada = input("Digite quantas pretas vão ao jogo: ").strip()
        # se quer permitir até 10 pretas, passe max=11;
        if verificacao(entrada, "preta", 10, 1) == 1:
            continue
        return int(entrada)

def montarTabuleiro(linhas, colunas):
    matrizTabuleiro.clear()
    for _ in range(linhas):
        matrizTabuleiro.append(["#"] * colunas)

def mostrarTabuleiro():
    for linha in matrizTabuleiro:
        print(" ".join(linha))
    print()

def existe_vizinho_preto(y, x, linhas, colunas):
    # recebe índices já 0-based: y = linha, x = coluna
    direcoes = [(-1,0),(1,0),(0,-1),(0,1)]
    for dy, dx in direcoes:
        ny, nx = y + dy, x + dx
        if 0 <= ny < linhas and 0 <= nx < colunas:
            if matrizTabuleiro[ny][nx] == "1":
                return True
    return False

def existe_vizinha_branca(y, x, linhas, colunas):
    direcoes = [(-1,0),(1,0),(0,-1),(0,1)]
    for dy, dx in direcoes:
        ny, nx = y + dy, x + dx
        if 0 <= ny < linhas and 0 <= nx < colunas:
            if matrizTabuleiro[ny][nx] == "0":
                return True
    return False

def colocarPreta(i, linhas, colunas):
    while True:
        try:
            entrada = input(f"Digite X e Y da {i+1}° Preta (formato: X Y): ").split()
            if len(entrada) != 2:
                print("Digite X e Y separados por espaço. Ex: 2 1")
                continue
            x, y = map(int, entrada)
        except ValueError:
            print("Digite apenas números inteiros. Tente novamente.")
            continue

        # convenção do usuário: X = coluna, Y = linha
        if x < 1 or x > colunas:
            print("Coordenada X (coluna) inexistente! Tente novamente.")
            continue
        if y < 1 or y > linhas:
            print("Coordenada Y (linha) inexistente! Tente novamente.")
            continue

        # ajusta para índices 0-based: y-1 = linha, x-1 = coluna
        if matrizTabuleiro[y-1][x-1] != "#":
            print("Já existe uma peça nessa posição! Tente outra.")
            continue

        matrizTabuleiro[y-1][x-1] = "1"
        break


def colocarBrancas(linhas, colunas):
    total = 0
    # estratégia gulosa: varre linha por linha; para cada célula vazia (#),
    # coloca '0' se houver ao menos uma preta vizinha e nenhuma branca vizinha já colocada.
    for y in range(linhas):
        for x in range(colunas):
            if matrizTabuleiro[y][x] != "#":
                continue
            if existe_vizinha_branca(y, x, linhas, colunas):
                continue
            if existe_vizinho_preto(y, x, linhas, colunas):
                matrizTabuleiro[y][x] = "0"
                total += 1
    return total

# ---------- programa principal ----------
while True:
    linhas = inputLinha()
    colunas = inputColuna()
    pretas = inputPretas()

    montarTabuleiro(linhas, colunas)

    for i in range(pretas):
        colocarPreta(i, linhas, colunas)

    print("Tabuleiro com pretas:")
    mostrarTabuleiro()

    totalBrancas = colocarBrancas(linhas, colunas)
    print("Tabuleiro final:")
    mostrarTabuleiro()
    print(f"Total de brancas: {totalBrancas}")

    break
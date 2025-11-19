#Importa a biblioteca easygui para usar caixas de diálogo gráficas
import easygui

#Cria um dicionário chamado teclado, onde cada chave é uma string e o valor é outra string com as letras que o nº representa.
#Serve para verificar se uma letra corresponde ao dígito do número.
teclado = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

#Abre uma caixa de diálogo que pede ao usuário para digitar o número de telefone.
N = easygui.enterbox("Digite o número de telefone (2–9):") #O valor digitado (texto) é atribuído à variável N como string. ex: 3482 == "3482"
M = int(easygui.enterbox("Quantas palavras quer testar?")) #Abre uma caixa de dialogo que pede quantas palavras o usuario quer testar easygui.enterbox retorna  texto e o int converte para inteiro o valor resultante é guardado em M.

#Cria uma lista vazia chamada palavras que vai guardar todas as palavras que o usuário digitar.
palavras = []
for i in range(M):  #começa um laço que se repete M vezes
    palavra = easygui.enterbox(f"Digite a palavra {i+1}:").lower() #mostra uma caixa pedindo a palavra número e lower transforma a palavra para letras minúsculas
    palavras.append(palavra) #adiciona a palavra digitada à lista palavras

#Inicializa o contador contagem com zero. Ele vai contar quantas palavras validas correspondem ao número.
contagem = 0
for palavra in palavras: #percorre cada palavra que o usuário forneceu.
    if len(palavra) != len(N): #verifica se o comprimento da palavra é igual ao comprimento do número.
        continue #se não for igual, pula para a próxima palavra
    combina = True #assume que a palavra combina até provar o contrário.
    for i in range(len(palavra)): #percorre cada posição i da palavra
        if palavra[i] not in teclado[N[i]]: #verifica se a letra combina com o número
            combina = False #se não combinar, marca como falsa
            break #e sai do laço (não precisa continuar verificando)

    if combina: #Se, no final, a palavra passou por todas as letras sem erro, ela combina e então
        contagem += 1 #soma 1 na contagem, pois essa palavra é válida

#Depois que todas as palavras foram testadas, o programa mostra uma janela dizendo quantas palavras combinam com o número.
easygui.msgbox(f"{contagem} palavra(s) correspondem ao número {N}.", "Resultado")

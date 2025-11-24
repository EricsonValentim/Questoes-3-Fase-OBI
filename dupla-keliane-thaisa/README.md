# Dupla-keliane-thaisa
Resolução do problema - Teclado.  (2021-3ª fase) - Olimpíada Brasileira de Informática

<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/1.png?raw=true)

<p align="right"</p>


### 💻 Ferramentas e Tecnologias que foram usadas

[![VSCode][VSCode]][VSCode-url]
[![Python][Python]][Python-url]
[![GitHub][GitHub]][GitHub-url]
[![EasyGUI][EasyGUI]][EasyGUI-url]

---

<!-- LINKS E ICONES -->

[VSCode]: https://img.shields.io/badge/VS%20Code-0078d7?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
[VSCode-url]: https://code.visualstudio.com/

[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/

[GitHub]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/

[EasyGUI]: https://img.shields.io/badge/EasyGUI-000000?style=for-the-badge&logo=python&logoColor=yellow
[EasyGUI-url]: https://easygui.readthedocs.io/en/master/

<!-- GETTING STARTED -->
## Entendendo o Problema

![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/2.png?raw=true)

---
### Entendendo as Entradas
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/3.png?raw=true)
---
### Entendendo a saída
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/4.png?raw=true)
---
### Entendendo os Limites do Programa
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/5.png?raw=true)
---

### Entradas do Código e Modelo Visual
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/7.png?raw=true)
---
### VS Code
Dentro do Vs Code a primeira coisa a se fazer é importar a biblioteca easygui para usar caixas de diálogo gráficas
* python
  ```sh
  import easygui
  ```
### 🔤Dicionário 
Cria um dicionário chamado teclado, onde cada chave é uma string e o valor é outra string com as letras que o nº representa.
Serve para verificar se uma letra corresponde ao dígito do número.
* python
  ```sh
  teclado = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
  }
  ```

### 💬Caixa de Diálogo
Abre uma caixa de diálogo que pede ao usuário para digitar o número de telefone. O valor digitado (texto) é atribuído à variável N como string. ex: 3482 == "3482". Abre uma caixa de dialogo que pede quantas palavras o usuario quer testar easygui.enterbox retorna  texto e o int converte para inteiro o valor resultante é guardado em M.
* python
  ```sh
  N = easygui.enterbox("Digite o número de telefone (2–9):") 
  M = int(easygui.enterbox("Quantas palavras quer testar?"))
  ```

### Processamento do Código e Modelo Visual
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/8.png?raw=true)

### ☑️Lista
A primeira linha cria uma lista vazia chamada palavras que  guarda todas as palavras que o usuário digitar. Na segunda linha começa um laço que se repete M vezes. Na terceira linha mostra uma caixa pedindo a palavra número e lower transforma a palavra para letras minúsculas. E na quarta linha será adicionado a palavra digitada à lista palavras
* python
  ```sh
  palavras = []
  for i in range(M):  
    palavra = easygui.enterbox(f"Digite a palavra {i+1}:").lower() 
    palavras.append(palavra)
  ```

### ⏰Contador
Inicializa o contador contagem com zero. Ele vai contar quantas palavras validas correspondem ao número. Depois na segunda linha o código percorre cada palavra que o usuário forneceu. Em seguida verifica se o comprimento da palavra é igual ao comprimento do número. Na próxima linha se não for igual, pula para a próxima palavra. Na quinta linha assume que a palavra combina até provar o contrário. Depois percorre cada posição i da palavra. Após isso verifica se a letra combina com o número e depois se não combinar, marca como falsa. E quando chega no break ele sai do laço (não precisa continuar verificando). No final, na parte do IF combina o código verifica Se, no final, a palavra passou por todas as letras sem erro, se ela combinar  então soma 1 na contagem, pois essa palavra é válida. 
* python
  ```sh
  contagem = 0
  for palavra in palavras: 
    if len(palavra) != len(N):
        continue 
    combina = True 
    for i in range(len(palavra)): 
        if palavra[i] not in teclado[N[i]]: 
            combina = False 
            break 

    if combina: 
        contagem += 1 
  ```

### Saídas do Código e Modelo Visual 
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/9.png?raw=true)

### 💻Resultado
Depois que todas as palavras foram testadas, o programa mostra uma janela dizendo quantas palavras combinam com o número.
* python
  ```sh
  easygui.msgbox(f"{contagem} palavra(s) correspondem ao número {N}.", "Resultado")
  ```

### Envio dos Arquivos via Git Bash
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/Captura%20de%20tela%202025-11-24%20094029.png?raw=true)

### Passo a Passo
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/Captura%20de%20tela%202025-11-24%20094125.png?raw=true)

### 💻Preparando para enviar
O git já estava configurado com email e usuário, após isso foi clonado o repositório destino e dentro dessa pasta foi iniciado o git bash. Em seguida foi copiado os arquivos da pasta local para dentro da pasta clonada, após isso foi feito o git status para analisar quais arquivos estariam sendo enviados e por fim, o envio: usando o comando (git add . ) que prepara os arquivos a serem enviados, por conseguinte (git commit -m "Mensagem") e finaliza com (git push) que envia as alterações para o repositório. 

### Final
![Imagem](https://github.com/divenanciodev/dupla-keliane-thaisa/blob/main/resolu%C3%A7%C3%A3o_teclado/3%C2%AAfase_2021/Explica%C3%A7%C3%A3oProblema/Captura%20de%20tela%202025-11-24%20094147.png?raw=true)






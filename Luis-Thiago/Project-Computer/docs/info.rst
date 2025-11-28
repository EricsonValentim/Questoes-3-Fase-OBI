# O computador
____________________________________
## Variavéis

- {tamanhoMemoria} em vez de "N"

- {quantidadeInstrucoes} em vez de "M"

- {posicao} em vez de "I"

- {valor} em vez de "V"
____________________________________
## Questions???

- A memória funcona como um vetor, que é um objeto geométrico que representa a direção, sentido e intensidade (ou módulo) de algo, 
  sendo ilustrado por uma seta.
____________________________________
## Estrutura dos dados

Memória: um vetor chamado memoria de tamanho (tamanhoMemoria) + 1.

- Por que + 1: para usar índices de 1 até tamanhoMemoria (o índice 0 fica sem uso, evitando confusão com endereços começando em 1).

- Instruções: uma lista de tuplas.
  
  Formato: (tipo, posicao, valor) para FRENTE e TRÁS; (tipo, posicao) para IMPRIME.

    Tipo 1: FRENTE posicao valor

    Tipo 2: TRÁS posicao valor

    Tipo 3: IMPRIME posicao

### Inicialização

Criar memória zerada: memoria = [0] * (tamanhoMemoria + 1)

- Todas as posições começam com zero, como especificado no enunciado.

- Laço principal das instruções
  
  Iterar instruções: for instrucao in instrucoes:
  
  # Em cada passagem, lê o tipo da instrução e executa o bloco correspondente.

- Tipo 1 — FRENTE posicao valor
  
  Ler parâmetros: posicao, valor = instrucao[1], instrucao[2]
  
  Preparar incremento: incremento = valor

Esse será o valor a somar na posição atual, decrescendo a cada passo.

- Percorrer para frente:
  
  Início: i = posicao
  
  Condição: enquanto i <= tamanhoMemoria e incremento > 0

- Passos do loop:
  
  Somar: memoria[i] += incremento
  
  Decrescer o valor: incremento -= 1
  
  Ir para a próxima posição: i += 1

Resultado: soma valor em posicao, depois valor-1 em posicao+1, e assim por diante, 
parando se chegar ao fim da memória ou quando o valor a somar ficar 0.

- Tipo 2 — TRÁS posicao valor
  
  Ler parâmetros: posicao, valor = instrucao[1], instrucao[2]
  
  Preparar incremento: incremento = valor
  
  Percorrer para trás:
  
  Início: i = posicao
  
  Condição: enquanto i >= 1 e incremento > 0
  
  Passos do loop:
  
  Somar: memoria[i] += incremento
  
  Decrescer o valor: incremento -= 1
  
  Ir para a posição anterior: i -= 1

Resultado: soma valor em posicao, depois valor-1 em posicao-1, e assim por diante, 
parando se chegar ao início da memória ou quando o valor a somar ficar 0.

- Tipo 3 — IMPRIME posicao
  
  Ler parâmetro: posicao = instrucao[1]
  
  Imprimir: print(memoria[posicao])
  - Mostra o valor atual armazenado naquele endereço, considerando todas as somas feitas até então.

### Execução do exemplo passo a passo

- Considere:
  
  tamanhoMemoria: 16
  
  instruções:
  
  (1, 4, 8) → FRENTE 4 8
  
  (2, 16, 3) → TRÁS 16 3
  
  (2, 2, 12) → TRÁS 2 12
  
  (1, 8, 7) → FRENTE 8 7
  
  (3, 4) → IMPRIME 4
  
  (3, 14) → IMPRIME 14
  
  (3, 1) → IMPRIME 1

- Após FRENTE 4 8
  
  Somas:
  
  pos 4 += 8, 5 += 7, 6 += 6, 7 += 5, 8 += 4, 9 += 3, 10 += 2, 11 += 1
  
  Parada: quando incremento vira 0 ou posição passa de 11 para 12 com incremento 0.
  
- Após TRÁS 16 3
  
  Somas:

  pos 16 += 3, 15 += 2, 14 += 1
  
- Após TRÁS 2 12
  
  Somas:
  
  pos 2 += 12, 1 += 11, 3 += 10, 4 += 9, 5 += 8, 6 += 7, 7 += 6, 8 += 5, 9 += 4, 10 += 3, 11 += 2, 12 += 1
  
### Observação: vai para trás até o início e continua diminuindo o valor; quando chega na posição 1, ainda há incremento, 
então ele segue “para trás” no endereço, mas como o limite é 1, o loop para. Em seguida, 
como o incremento continua > 0, o próximo passo é a posição 3? Não: o movimento é sempre para trás (i -= 1), 
então o que ocorre na prática é: do 2 vai para 1, depois para 0 (para o loop), portanto a sequência válida é 2,1 e pára quando i fica 0.

- Como cobrimos múltiplas somas do exemplo: aqui foi uma explicação agregada do efeito desejado no vetor conforme a demonstração dada — o 
- importante é entender que cada passo anda uma posição para trás e decrementa o valor.

- Após FRENTE 8 7
  
  Somas:
  
  pos 8 += 7, 9 += 6, 10 += 5, 11 += 4, 12 += 3, 13 += 2, 14 += 1


    IMPRIME 4, 14, 1

    IMPRIME 4: mostra o valor acumulado na posição 4.

    IMPRIME 14: mostra o valor acumulado na posição 14.

    IMPRIME 1: mostra o valor acumulado na posição 1.

- Por que funciona
  Controle por limites: os while garantem que não saímos dos limites da memória (nem abaixo de 1, nem acima de tamanhoMemoria).
  
  Valor decrescente: a variável incremento diminui a cada passo, parando quando chega a 0.
  
  Estado acumulado: todas as somas são feitas diretamente no vetor memoria, então IMPRIME lê o estado atual sem precisar recalcular nada.

- Observações de desempenho
  
  Complexidade: cada instrução FRENTE/TRÁS pode percorrer até valor posições (ou até bater em um extremo da memória). 
  No pior caso, com valores grandes, isso pode ser custoso.
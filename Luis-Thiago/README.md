## 📘 Structured Git/GitHub usage — OBI Programming Project

The goal of this project is to showcase solutions to OBI (Brazilian Informatics Olympiad) problems, computer-related tasks, and random chess challenges, all implemented in Python. It also serves as an example of using Git for project and repository management.
______________________________________
## 📑 Table of Contents

- [About the Project](#-about-the-project)

- [Problem Description](#-problem-description)

- [OBI Context](#-obi-context)

- [Approach & Solution](#-approach--solution)

- [Algorithm Explanation](#-algorithm-explanation)

- [How to Run](#️-how-to-run)

- [Input & Output Examples](#-input--output-examples)

- [Project Structure](#-project-structure)

- [Testing](#-testing-execution-with-git)

- [Git Workflow](#-git-workflow)

- [References](#-references)

- [License](#-license)
_______________________________________
## 📘 About the Project

    This repository contains the source code and explanation for solving the OBI problem “Computer” (year 2019, phase 3) and “Chess” (year 2019, phase 3).
______________________________________

## 📝 Problem Description

what will be described?

    - The task
    - Inputs/Outputs
    - Constraints

---
# Problem 1 Computer

### OBI Memory Instructions Simulator

A large company is designing a new computer architecture that supports two efficient special addition instructions. The computer contains **N memory positions**, indexed from **1 to N**, and each position stores a non‑negative integer. Initially, all memory positions contain zero.

## 📌 Special Addition Instructions

### **FRENTE i V**

Given an address `i` (where `1 ≤ i ≤ N`) and a positive value `V`, the computer must:

* Add `V` to position `i`,
* Add `V-1` to position `i+1`,
* Add `V-2` to position `i+2`,
* And so on...

This continues while the value being added is greater than zero **and** the memory position does not exceed `N`.

### **TRÁS i V**

Given an address `i` (where `1 ≤ i ≤ N`) and a positive value `V`, the computer must:

* Add `V` to position `i`,
* Add `V-1` to position `i-1`,
* Add `V-2` to position `i-2`,
* And so forth...

This continues while the value being added is greater than zero **and** the memory position is at least `1`.

## 📘 Example (N = 16)

Below is an example execution sequence:

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

FRENTE 4 8
0 0 0 8 7 6 5 4 3 2 1 0 0 0 0 0

TRÁS 16 3
0 0 0 8 7 6 5 4 3 2 1 0 0 1 2 3

TRÁS 2 12
11 12 0 8 7 6 5 4 3 2 1 0 0 1 2 3

FRENTE 8 7
11 12 0 8 7 6 5 11 9 7 5 3 2 2 2 3
```

## 🖨️ Print Instruction

### **IMPRIME i**

This instruction prints the current value stored at memory position `i`.

## 🎯 Objective

Given `N` and a sequence of `M` instructions, your program must:

* Process each instruction in order,
* And for every `IMPRIME i` instruction,
* Output the value at memory position `i` **at that moment**.

## 🧩 Notes

* All memory positions start with value **0**.
* Values never become negative.
* The instructions may overlap in their effects.

## 📥 Input

The first line of input contains two integers `N` and `M`, representing the number of memory positions and the number of instructions, respectively.

Each of the next `M` lines contains one instruction in one of the following formats:

* `1 I V` — represents **FRENTE I V**
* `2 I V` — represents **TRÁS I V**
* `3 I` — represents **IMPRIME I**

## 📤 Output

For every instruction of type `IMPRIME I`, the program must output a line containing the integer value currently stored at memory position `I` at the moment the instruction is executed.

## 🔒 Constraints

* `1 ≤ N ≤ 200000`
* `1 ≤ M ≤ 200000`
* `1 ≤ I ≤ N`
* `1 ≤ V ≤ 200000`
* At least one instruction will be of type `3` (IMPRIME)

## 🛠️ Possible Extensions

* Implementing an optimized solution using prefix differences.
* Adding validation for instruction formats.
* Supporting batch execution and benchmarking.

#### [Link](https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/computador/) the official Site.
---
_______________________________________
# Problem 2 Chess

### Chess960 Simplified Variant — Valid Starting Positions

Fischer Random Chess, or **Chess960**, is a chess variant that follows all the traditional rules of Chess with one exception: the initial arrangement of the pieces is randomized before play begins. The pieces on the back rank may appear in any order as long as two constraints are met:

* The king must be placed between the two rooks.
* The two bishops must occupy opposite-colored squares.

As the name suggests, this leads to exactly **960 valid starting positions**.

In this problem, we consider a much simpler variant. The size of the board is no longer fixed. For any board dimension `N`, the first row contains only three types of pieces:

* King (exactly one)
* Rook (zero, one, or two)
* Pawn (all remaining positions)

If there are **two rooks**, the king must be placed **between** them. The number of pawns is equal to the board dimension minus the number of other pieces. Below is an example of a valid starting position for `N = 8`.

## 📥 Input

The input consists of a single line containing two integers:

* `N` — the board dimension
* `T` — the number of rooks (0 to 2)

## 📤 Output

Your program must output a single integer representing the number of valid starting positions.

## 🔒 Constraints

* `2 ≤ N ≤ 1000`
* `0 ≤ T ≤ 2`

#### [Link](https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/xadrez/) the official Site.
---
_______________________________________
## 🏅 OBI Context

Add contextual information:

- OBI category: Programação Nível Sênior

- Phase: Third

- Key topics covered (Ordering, dynamic programming, simulation)
_______________________________________
## 🔍 Abordagem e Solução

### Computer project:
    Percorrer a memória diretamente, atualizando posição por posição, simulando passo a passo cada instrução exatamente como descrita.

    FRENTE i V: soma V, V-1, V-2... avançando para a direita, até o valor acabar ou atingir o fim da memória.

    TRÁS i V: soma V, V-1, V-2... avançando para a esquerda, até o valor acabar ou atingir o início da memória.

    IMPRIME i: simplesmente exibe o valor atual armazenado na posição i.

    - Ou seja:
        Sem atalhos

        Sem estruturas avançadas

        Sem otimizações

    ✔ Características:
    
    - Fácil de entender
    - Fácil de implementar
    - Porém lenta para valores muito grandes

### Chess project:

    O programa calcula quantas posições iniciais válidas existem em um tabuleiro de dimensão N contendo:

    ```bash
    1 rei

    0, 1 ou 2 torres
    ```
    - o restante preenchido com peões

    A escolha da fórmula depende apenas do número de torres T, sem usar loops ou simulações.

    - Regras usadas

    T = 0 → o rei pode ocupar qualquer posição
    resultado = N

    T = 1 → escolher posições distintas para rei e torre
    resultado = N * (N - 1)

    T = 2 → rei deve ficar entre as duas torres
    Fórmula combinatória:
    resultado = N * (N - 1) * (N - 2) / 6

    ✔ Características

    - Sem loops

    - Sem gerar tabuleiros

    - Uso direto de fórmulas combinatórias

    - Execução instantânea mesmo para N = 1000
---
_______________________________________
## 📐 Algorithm Explanation

A more detailed section:

- ✅ Pseudocódigo 1 — executar_instrucoes
```bash
Algoritmo ExecutarInstrucoes
    Entrada: tamanhoMemoria, instrucoes

    // Inicialização da memória
    Criar vetor MEMORIA de 1 até tamanhoMemoria
    Para i de 1 até tamanhoMemoria faça
        MEMORIA[i] ← 0
    FimPara

    // Processamento das instruções
    Para cada INSTRUCAO em instrucoes faça
        TIPO ← INSTRUCAO[0]

        Se TIPO = 1 então                  // FRENTE posicao valor
            POSICAO ← INSTRUCAO[1]
            INCREMENTO ← INSTRUCAO[2]
            i ← POSICAO

            Enquanto (i ≤ tamanhoMemoria) e (INCREMENTO > 0) faça
                MEMORIA[i] ← MEMORIA[i] + INCREMENTO
                INCREMENTO ← INCREMENTO - 1
                i ← i + 1
            FimEnquanto

        Senão se TIPO = 2 então            // TRÁS posicao valor
            POSICAO ← INSTRUCAO[1]
            INCREMENTO ← INSTRUCAO[2]
            i ← POSICAO

            Enquanto (i ≥ 1) e (INCREMENTO > 0) faça
                MEMORIA[i] ← MEMORIA[i] + INCREMENTO
                INCREMENTO ← INCREMENTO - 1
                i ← i - 1
            FimEnquanto

        Senão se TIPO = 3 então            // IMPRIME posicao
            POSICAO ← INSTRUCAO[1]
            Escrever MEMORIA[POSICAO]

        FimSe
    FimPara
FimAlgoritmo
```

- ✅ Pseudocódigo 2 — Contagem de posições (Português Estruturado)
```bash
Algoritmo ContarPosicoes
    Ler N, T

    Se T = 0 então
        // Apenas o rei: qualquer uma das N casas
        RESULTADO ← N

    Senão se T = 1 então
        // Rei e uma torre: devem ocupar posições diferentes
        RESULTADO ← N * (N - 1)

    Senão                    // T = 2
        // Duas torres e o rei entre elas
        RESULTADO ← (N - 2) * (N - 1) * N / 6
    FimSe

    Escrever RESULTADO
FimAlgoritmo
```
---
_______________________________________
## ▶️ How to Run

Requirements

- Language (Python)

- Version requirements (Python 3.10…)

### Running the program Computer
    
- In Python
```bash
    C:/Users/$USER/AppData/Local/Programs/Python/Python314/python.exe c:/Users/$USER/Project-codiname-IC/project-computer/src/main.py
```
### Running the program Chess

- In Python
```bash
    C:\Users\$USER\Project-codiname-IC> & C:/Users/$USER/AppData/Local/Programs/Python/Python314/python.exe c:/Users/$USER/Project-codiname-IC/project-Xadrez/src/main.py
```

_______________________________________
## 📥 Input & Output Examples

- Example Computer:

Input:
```bash
tamanhoMemoria = 16
instrucoes = [
    (1, 4, 8),   # FRENTE 4 8
    (2, 16, 3),  # TRÁS 16 3
    (2, 2, 12),  # TRÁS 2 12
    (1, 8, 7),   # FRENTE 8 7
    (3, 4),      # IMPRIME 4
    (3, 14),     # IMPRIME 14
    (3, 1)       # IMPRIME 1
]
```
Output:
```bash
8
2
11
```
---
- Example Chess:

Input:
```bash
8 #Posição da casa 
1 #Nº da Peça; Torre
```
Output:
```bash
56 #Combinações possíveis
```
________________________________________
## 📁 Project Structure

- Example structure:

```repo
Project/
 ├── docs/
 │    └── info.rst
 ├── src/
 │    └── main.py
 ├── test/
 │    └── expected.txt
 │    └── input.txt
 │    └── output.txt
 ├── README.md
 └── LICENSE
```

________________________________________
## 🧪 Testing Execution with Git

Explain how to test the solution manually or automatically.

Example:
```exp
./test/input1.txt
```
### ⚠️ Problems During Development

The most common issue when using Git/GitHub was the merge sequence, which is the process of combining the changes from one branch into another.

- Exemplo:
```bash
C:\Users\$USER\Project-codiname-IC> git push To https://github.com/cost-12/Project-codiname-IC.git ! [rejected] main -> main (non-fast-forward) error: failed to push some refs to 'https://github.com/cost-12/Project-codiname-IC.git' hint: Updates were rejected because the tip of your current branch is behind hint: its remote counterpart. If you want to integrate the remote changes, hint: use 'git pull' before pushing again. hint: See the 'Note about fast-forwards' in 'git push --help' for details. PS C:\Users\$USER\Project-codiname-IC> git pull error: You have not concluded your merge (MERGE_HEAD exists). hint: Please, commit your changes before merging. fatal: Exiting because of unfinished merge. PS C:\Users\$USER\Project-codiname-IC>
```
    This happens when you're stuck in an unfinished merge state, which prevents you from doing either git pull or git push

### Solution

✅ Passo 1 — Verificar o estado atual
```bash
#Execute:

$ git status
```
Você deve ver algo como:
You are in the middle of a merge
____

✅ Passo 2 — Concluir o merge que está pendente

Se você quer manter suas alterações locais:
```bash
# Adicionar e concluir o merge
$ git add .
$ git commit -m "Conclui merge pendente"
```
This completes the incomplete merge.
___

✅ Passo 3 — Agora sim, sincronizar com o servidor
```bash
# Após concluir o merge:

git pull --rebase

# ou, se preferir sem rebase:

git pull

# Se não vier mais nada, finalize:

git push
```
# Opcional:

⭐ Atalho para resolver rápido (se você não tem alterações importantes)

⚠️ Só use se você quiser descartar alterações locais!
```bash
git merge --abort
git reset --hard origin/main
```
Isso força seu repositório local a ficar idêntico ao remoto.
________________________________________
## 📘 Git Workflow

- Clone repository
```bash
git clone https://github.com/cost-12/Project-codiname-IC.git
cd Project-codiname-IC
```

- Inicicialized repository
```bash
git init
```

-  Adicioned informations
```bash
git add .
```

- Commit informations
```bash
git commit -m "version"
```

- Upload informations commit
```bash
git push -u origin main (first time)
```
________________________________________
## 📚 References
- Official [OBI](https://olimpiada.ic.unicamp.br/pratique/pu/) website
- Using collaborative git [Atlassiam](https://www.atlassian.com/git)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
________________________________________
## 📄 License

- [Unlicense license](https://unlicense.org)
LICENSE
---
[(Back to top)](#-table-of-contents)

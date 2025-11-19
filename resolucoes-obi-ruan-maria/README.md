# 🧠 Resoluções OBI – Dupla Maria de Jesus e Ruan Carlos

Este diretório contém as resoluções desenvolvidas pela dupla **Maria de Jesus e Ruan Carlos** para questões da **1º e 3ª Fase da Olimpíada Brasileira de Informática (OBI)**.  
As soluções foram implementadas em **Python**, com foco em simplicidade, clareza e boa lógica.

---

## 📚 Objetivo

Organizar, registrar e compartilhar as resoluções de problemas da OBI, mantendo um padrão limpo de código, versionamento correto via Git e documentação clara para estudo e revisão futura.

---

## 📂 Estrutura da Pasta

resolucoes-obi-ruan-maria/
├── zero_para_cancelar.py
├── ogro.py
└── README.md

---

# 🟦 Questão 01 – Zero para Cancelar

### 🔍 Descrição

Nesta questão, seu chefe informa números por telefone.  
Sempre que ele diz **0**, isso significa **desfazer o último número informado**.

Seu objetivo é calcular **a soma final** dos números válidos após considerar os cancelamentos.

---

### 🧠 Ideia da Solução

Foi utilizada a lógica de uma **pilha (stack)**:

- Quando o número é **não-zero**, adicionamos na pilha com `append()`
- Quando o número é **zero**, removemos o último com `pop()`
- Ao final, somamos todos os valores restantes

Esse é exatamente o comportamento de desfazer/voltar.

---

### ▶️ Como executar a solução

Caso queira testar com entrada manual:

```bash
python3 quest01_zero_para_cancelar.py
```

- Ou usando um arquivo de entrada:

```python3 zero_para_cancelar.py < entrada.txt
```

# 🟩 Questão 02 – Ogro

### 🔍 Descrição

O Ogro conta números usando os dedos das mãos:

Cada dedo é representado pela letra I

A mão fechada é representada por *

Regras:

- Para números de 0 a 5, ele usa apenas a mão esquerda;
- Para números de 6 a 10, a mão esquerda mostra 5 dedos, e a mão direita mostra o restante.

# 🧠 Ideia da Solução

- Se N == 0 → * e *

- Se 1 ≤ N ≤ 5 → "I" * N e *

- Se 6 ≤ N ≤ 10 → "IIIII" e "I" * (N - 5)

# ▶️ Como executar a solução

```python3 ogro.py
``
# 🧠 Resoluções OBI – Dupla Maria de Jesus e Ruan Carlos

Este diretório contém as resoluções desenvolvidas pela dupla **Maria de Jesus e Ruan Carlos** para questões da **1º e 3ª Fase da Olimpíada Brasileira de Informática (OBI)**.  
As soluções foram implementadas em **Python**, com foco em clareza, lógica e evolução progressiva dos conceitos.

---

## 📚 Objetivo

Organizar, registrar e compartilhar as resoluções de problemas da OBI, mantendo um padrão limpo de código, versionamento correto via Git e documentação clara para estudo e revisão futura.

---

## 📂 Estrutura da Pasta

resolucoes-obi-ruan-maria/
├── quest01_zero_para_cancelar.py
├── quest02_cinco.py (em desenvolvimento)
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
```python3 quest01_zero_para_cancelar.py




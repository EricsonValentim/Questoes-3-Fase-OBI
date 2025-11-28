## 📌 Workflow de Uso do Git/GitHub

Este projeto segue um fluxo de trabalho simples e organizado para facilitar colaboração, controle de versão e rastreamento de mudanças.  
Abaixo está o fluxo recomendado:

---

# Table of contents
- [Configuração Inicial](#-1-configuração-inicial)
- [Fluxo de Trabalho](#-fluxo-de-trabalho)
- [Estrutura de Teste](#-estrutura-de-testes-opcional)
- [Criar Branchs para trabalho](#-2-criar-uma-nova-branch-para-trabalhar)
- [Realizar Alterações](#-3-fazer-alterações-no-código)
- [Confirmar alterações](#-4-adicionar-e-confirmar-alterações-commit)
- [Enviar Alterações](#-5-enviar-alterações-para-github-push)
- [Abrir Pull Request](#-6-abrir-um-pull-request)
- [Revisão](#-7-revisão-e-aprovação)
- [Atualizar Arquivos Locais](#-8-atualizar-sua-máquina-local)
- [Badges](#badges)

---

### 🔧 1. **Configuração Inicial**

1. Instale o Git (Linux, Windows ou macOS)
2. Configure suas credenciais:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```
Este projeto utiliza um fluxo de trabalho simples e eficiente para manter o código organizado, estável e fácil de versionar.
---

### 🔄 Fluxo de Trabalho

#### **1. Atualizar a branch main**
```bash
git checkout main
git pull origin main
```
#### **2. Criar uma nova branch**
```bash
git checkout -b feature/nova-funcionalidade
```
#### **3. Fazer alterações e criar commits**
```bash
git add .
git commit -m "feat: adicionar operação FRENTE"
```
#### **4. Enviar a branch para o GitHub**
```bash
git push origin feature/nova-funcionalidade
```
_______________________________________________
### 🧪 Estrutura de Testes (Opcional)
```estruture
tests/
 ├── input1.txt
 ├── expected1.txt
 ├── input2.txt
 └── expected2.txt
```
_______________________________________________
## 🌿 2. Criar uma nova branch para trabalhar

Sempre crie uma branch nova antes de começar uma funcionalidade ou correção:
```bash
git checkout -b nome-da-feature
```

- **main** → código estável  
- **feature/<nome>** → novas funcionalidades  
- **fix/<nome>** → correções de bugs  
- **test/<nome>** → experimentos e testes opcionais  

Exemplos:
```exemplo
feature/adição-instrucoes
fix/corrigir-index
test/algoritmo-novo
```
---
---

## 💻 3. Fazer alterações no código

Edite, implemente funções, adicione testes etc.

- Para verificar o status:
```bash
git status
```
---

## 📥 4. Adicionar e confirmar alterações (commit)

Adicione as mudanças:
```bash
git add .
```
Faça um commit claro e descritivo:
```bash
git commit -m "Implementa lógica de execução das instruções FRENTE/ATRAS"
```
---

## ⬆ 5. Enviar alterações para GitHub (push)
```bash
git push origin nome-da-feature
```
---

## 🔀 6. Abrir um Pull Request

Opicional:
- Crie uma nova branch com git checkout -b <nome-da-branch> para trabalhar em uma nova funcionalidade ou correção sem afetar a branch principal. 
---
- Vá até o GitHub.
    Abra um Pull Request da sua branch → main.

Descreva:
```description

- O que foi feito?

- Por que?

- Como testar?
```
---

## 🧪 7. Revisão e aprovação

Outro colaborador revisa o PullRequest.

Podem haver comentários ou ajustes necessários.

Após aprovado, o PR é mergeado na main.

---

## 🧹 8. Atualizar sua máquina local

Após o merge:
```bash
git checkout main
git pull origin main
```
E delete a branch antiga:
```bash
git branch -d nome-da-feature
```
---

## 🔄 9. Ciclo se repete

- Crie uma nova feature → programe → commit → push → PR → merge.
---
## ✨ 10. Extra

- Habilite a sensibilidade a maiúsculas/minúsculas:
````bash
git config core.ignorecase false
````
---
# Badges

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

[(Back to top)](#table-of-contents)
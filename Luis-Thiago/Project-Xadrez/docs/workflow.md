## 🔄 9. Ciclo Básico

Adicione as mudanças:
```bash
git add .
```
Faça um commit claro e descritivo:
```bash
git commit -m "Implementa lógica de execução das instruções FRENTE/ATRAS"
```
---

### ⬆ Enviar alterações para GitHub (push)
```bash
git push origin nome-da-feature
```
---

```bash
git checkout main
git pull origin main
```
E delete a branch antiga:
```bash
git branch -d nome-da-feature
```
---

1. Mudar para uma branch existente
Este é o uso mais comum. Ele alterna o seu diretório de trabalho para a branch especificada, exatamente como o git checkout faria.

```bash
git switch nome-da-branch
```
- Exemplo: Para voltar para a branch principal do seu projeto:
```bash
git switch main
```
---
2. Criar uma nova branch e mudar para ela
A flag -c (de create) permite que você crie uma nova branch com o nome especificado e mude para ela automaticamente, tudo em um único comando. Isso substitui o comum git checkout -b.
````bash
git switch -c novo-nome-da-branch
````

### Passos para unificar com git merge:
Vá para a branch de destino:
Primeiro, mude para a branch que você deseja atualizar com as alterações da outra branch. Por exemplo, se você quer trazer alterações da branch feature-x para a main, você deve estar na main:
````bash
git switch main
# ou o antigo: git checkout main
````
---

### Execute o comando de merge:
Agora, diga ao Git para trazer as alterações da feature-x para dentro da sua branch atual (main):
````bash
git merge feature-x
````
---
Resolva conflitos (se houver):
Se o Git encontrar linhas de código que foram modificadas de maneiras diferentes em ambas as branches (conflito de merge), ele pausará a operação e pedirá que você resolva o conflito manualmente.
- Finalize:

    Após resolver quaisquer conflitos e salvar os arquivos, use git add . e git commit para finalizar o commit de merge. 

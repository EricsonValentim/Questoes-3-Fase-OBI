# Como corrigir o problema de nome de pastas não serem identificadas no Windows???

✅ 1. Liste o nome exato das pastas que o Git está versionando

- No PowerShell, rode:
```bash
ls
```
ou:
```bash
git ls-files --stage
```
- O Git está enxergando as pastas assim:
```bash
project-computer
project-Xadrez
```

Ou seja — tudo minúsculo no primeiro caso, e “X” maiúsculo no segundo.

## Por exemplo:

➡️ A pasta localmente aparece como Project-Computer,
➡️ Mas para o Git, o nome REAL é project-computer.

Como o Git não considera mudanças apenas de maiúsculas/minúsculas no Windows, precisamos forçar a alteração.

### Para resolver;
1️⃣ Renomear para um nome temporário (para o Git enxergar mudança)
git mv project-computer project-computer-temp

2️⃣ Depois renomear para o nome desejado
git mv project-computer-temp Project-Computer

🔄 Repita o mesmo para project-Xadrez se quiser padronizar para Project-Xadrez:
git mv project-Xadrez project-xadrez-temp
git mv project-xadrez-temp Project-Xadrez

📌 Depois disso:

Finalize:

git commit -m "Fix folder names (case sensitivity)"
git push

💡 Por que isso funciona?

O Git só registra mudança se:

mudar totalmente o nome (mesmo que temporário)

depois mudar para o nome final

Windows não é case-sensitive → sem esse truque, o Git ignora a mudança.
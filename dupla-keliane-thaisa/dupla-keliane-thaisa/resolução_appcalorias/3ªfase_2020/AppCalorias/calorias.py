import easygui as eg


titulo = " Calculadora de Calorias"

while True:
    
    campos = ["E1 (mínimo)", "E2 (máximo)", "E3 (alternativo)", "X (diferença limite)"]
    valores = eg.multenterbox(
        "Digite os valores abaixo para estimar as calorias da refeição:",
        titulo,
        campos
    )

    
    if valores is None:
        eg.msgbox("Programa encerrado.", titulo)
        break

    try:
        E1, E2, E3, X = map(int, valores)

       
        if (E2 - E1) <= X:
            resultado = E2
        else:
            resultado = E3

        eg.msgbox(
            f" Calorias estimadas: {resultado}\n\n(E1={E1}, E2={E2}, E3={E3}, X={X})",
            titulo
        )

    except ValueError:
        eg.msgbox("⚠️ Por favor, insira apenas números inteiros válidos.", "Erro")

    if not eg.ynbox("Deseja realizar outro cálculo?", titulo, ("Sim", "Não")):
        eg.msgbox("Até logo!", titulo)
        break

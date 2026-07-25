'''
    PMV 1.0 - Processador Contínuo de Folha de Pagamento
    Conceito: Introdução ao laço 'while True' e acumuladores de estado na memória.
'''

print("=== PROCESSADOR DE FOLHA TECHSOLUTION v1.0 ===")

# Variável Acumuladora (Mantém o estado fora do ciclo)
total_folha = 0.0

# Laço infinito: O código recomeça aqui automaticamente
while True:
    nome = input("\nNome do Colaborador: ").strip()
    #nome = input("\nNome do Colaborador: ").strip()
    salario_base = float(input("Salario Base (R$): "))
    bonus = float(input("Bônus de Meta (R$): "))

    salario_final = salario_base + bonus
    total_folha += salario_final # Somando ao acumulador global

    print(f"\n-> Holerite calculado: {nome} | Líquido: R$ {salario_final:.2f}")

    # Condição de Parada do Ciclo
    continuar = input("\nDeseja processar outro colaborador? [S/N]: ").strip().upper()
    if continuar == "N":
        break # Quebra e encerra o laço 'while' imediatamente

print(f"\n=== FECHAMENTO DO LOTE ===\nTotal Acumulado na Folha: R$ {total_folha:.2f}")
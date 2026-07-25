"""
PMV 2.0 - Processador Contínuo de Folha de Pagamento
Conceito: Menu numérico, while True, acumuladores e tratamento de exceções.
"""

print("=== PROCESSADOR DE FOLHA TECHSOLUTIONS v2.0 ===")

# Acumulador global
total_folha = 0.0

while True:
    print("\n===== MENU PRINCIPAL =====\n")
    print("[1] Cadastrar Colaborador")
    print("[2] Ver Total Acumulado")
    print("[3] Encerrar Sistema")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":

        try:
            nome = input("\nNome do Colaborador: ").strip()

            salario_base = float(
                input("Salário Base (R$): ").replace(",", ".")
            )

            bonus = float(
                input("Bônus de Meta (R$): ").replace(",", ".")
            )

            salario_final = salario_base + bonus
            total_folha += salario_final

            print(
                f"-> Holerite calculado: "
                f"{nome} | Líquido: R$ {salario_final:.2f}"
            )

        except ValueError:
            print(
                "\n[ERRO] Valor numérico inválido. "
                "Operação cancelada, retornando ao menu."
            )

    elif opcao == "2":

        print("\n=== CONSULTA DE ACUMULADO ===")
        print(f"Total acumulado na folha: R$ {total_folha:.2f}")

    elif opcao == "3":

        print("\n=== FECHAMENTO DO LOTE ===")
        print(f"Total Acumulado na Folha: R$ {total_folha:.2f}")
        print("Sistema encerrado com sucesso.")
        break

    else:

        print("\n[ERRO] Opção inválida. Escolha 1, 2 ou 3.")

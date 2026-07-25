"""
PMV 3.0 - Processador Contínuo de Folha de Pagamento

Recursos:
- Menu numérico
- Acumulador em memória
- Tratamento de exceções
- Persistência em CSV
- Persistência em JSON
"""

def formatar_moeda(valor):
    return (
        f"{valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

import csv
import json
import os

print("=== PROCESSADOR DE FOLHA TECHSOLUTIONS v3.0 ===")

ARQUIVO_CSV = "folha_lote.csv"
ARQUIVO_JSON = "folha_lote.json"

# Acumulador global
total_folha = 0.0

# Lista que será gravada no JSON
registros_json = []

# Cria cabeçalho CSV na primeira execução
if not os.path.exists(ARQUIVO_CSV):
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            ["Nome", "Salario_Base", "Bonus", "Salario_Final"]
        )

while True:

    print("\n===== MENU PRINCIPAL =====")
    print("[1] Cadastrar Colaborador")
    print("[2] Ver Total Acumulado")
    print("[3] Encerrar Sistema")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":

        try:
            nome = ' '.join(input("\nNome do Colaborador: ")).strip()

            salario_base = float(
                input("Salário Base (R$): ").replace(",", ".")
            )

            bonus = float(
                input("Bônus de Meta (R$): ").replace(",", ".")
            )

            salario_final = salario_base + bonus
            total_folha += salario_final

            #salario_formatado = f"{salario_final:.2f}".replace(".", ",")

            #separador com padrão brasileiro
            #salario_formatado = f"{salario_final:,.2f}" \
            #    .replace(",", "X") \
            #    .replace(".", ",") \
            #    .replace("X", ".")

            #print(
            #    f"\n-> Holerite calculado: "
            #    f"{nome} | Líquido: R$ {salario_formatado}"
            #)

            #print(
            #                f"\n-> Holerite calculado: "
            #                f"{nome} | Líquido: R$ {salario_final:.2f}"
            #            )
            
            print(
                f"\n-> Holerite calculado: "
                f"{nome} | Líquido: R$ {formatar_moeda(salario_final)}"
            )

            # -----------------------------
            # REGISTRO CSV
            # -----------------------------
            with open(
                ARQUIVO_CSV,
                mode="a",
                newline="",
                encoding="utf-8"
            ) as arquivo_csv:

                escritor = csv.writer(arquivo_csv, delimiter= ";")

                escritor.writerow([
                    nome,
                    salario_base,
                    bonus,
                    salario_final
                ])

            # -----------------------------
            # REGISTRO JSON
            # -----------------------------
            registro = {
                "nome": nome,
                "salario_base": salario_base,
                "bonus": bonus,
                "salario_final": salario_final
            }

            registros_json.append(registro)

            with open(
                ARQUIVO_JSON,
                mode="w",
                encoding="utf-8"
            ) as arquivo_json:

                json.dump(
                    registros_json,
                    arquivo_json,
                    indent=4,
                    ensure_ascii=False
                )

            print("Registros salvos em CSV e JSON.")

        except ValueError:

            print(
                "\n-*- ERRO -*-\nValor numérico inválido."
                "\nOperação cancelada e retorno ao menu.\n-*- ERRO -*-                   "
            )


    elif opcao == "2":

        print("\n=== CONSULTA DE ACUMULADO ===")
        #print(f"Total acumulado na folha: R$ {total_folha:.2f}")
        print(f"Total acumulado na folha: R$ {formatar_moeda(total_folha)}")

    elif opcao == "3":

        print("\n=== FECHAMENTO DO LOTE ===")
        #print(f"Total Acumulado na Folha: R$ {total_folha:.2f}")       
        print(f"Total Acumulado na Folha: R$ {formatar_moeda(total_folha)}")
        print("Sistema encerrado com sucesso.")
        break

    else:

        print("\n-*- ERRO -*-\nOpção inválida. Escolha 1, 2 ou 3.\n-*- ERRO -*-\n")

"""
Desenvolvimento inicial focado exclusivamente na lógica de negócio.
Refatorado com tratamento de exceções e otimização dos condicionais.
"""

print("=== SISTEMA DE AUDITORIA FINANCEIRA V1.0 ===")
print("Iniciando captura de dados...\n")

try:
    categoria_texto = input(
        "Digite a categoria\n(transporte/alimentação/hospedagem): "
    )
    categoria = categoria_texto.strip().lower()

    valor_texto = input("\nDigite o valor do gasto (R$): ")
    valor_formatado = valor_texto.replace(",", ".")

    valor = float(valor_formatado)

    print("\n... Processando regras do compliance ...\n")

    if valor <= 0:
        print("Parecer: NEGADO - valor deve ser maior que zero.")

    elif categoria == "transporte":
        if valor <= 150.0:
            print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de transporte.")
        else:
            print("Parecer: REQUER ANÁLISE - ultrapassou o teto de transporte.")

    elif categoria == "alimentação":
        if valor <= 85.0:
            print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de alimentação.")
        else:
            print("Parecer: REQUER ANÁLISE - ultrapassou o teto de alimentação.")

    elif categoria == "hospedagem":
        if valor <= 450.0:
            print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de hospedagem.")
        else:
            print("Parecer: REQUER ANÁLISE - ultrapassou o teto de hospedagem.")

    else:
        print("Parecer: NEGADO - categoria não reconhecida.")

except ValueError:
    print("\nErro: valor monetário inválido. \n"
        "Digite apenas números, por exemplo: 150 ou 150,50.")

finally:
    print("\n... Auditoria finalizada ...\n")

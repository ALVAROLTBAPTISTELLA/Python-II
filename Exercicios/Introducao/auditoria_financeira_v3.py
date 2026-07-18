"""
SISTEMA DE AUDITORIA FINANCEIRA V3.0
- Tratamento de exceções
- Captura de Nome e Cargo
- Exibição de política interna
- Gravação de relatório em arquivo texto
"""

print("=== SISTEMA DE AUDITORIA FINANCEIRA V3.0 ===")

print("\nPOLÍTICA INTERNA DE REEMBOLSO")
print("+" + "-" * 58 + "+")
print("| CATEGORIA      | TETO MÁXIMO (R$)"+ " " * 24 +  "|")
print("-" * 60)
print("| Transporte     | 150.00")
print("| Alimentação    | 85.00")
print("| Hospedagem     | 450.00")
print("-" * 60)

print("\nCARGOS ACEITOS")
print("-" * 60)
print(" - Analista")
print(" - Supervisor")
print(" - Gerente")
print(" - Diretor")
print("-" * 60)

parecer = "NÃO PROCESSADO"

try:
    print("\n=== IDENTIFICAÇÃO DO SOLICITANTE ===")

    nome = input("Nome do solicitante: ").strip()

    cargo = input(
        "Cargo (Analista/Supervisor/Gerente/Diretor): "
    ).strip().title()

    categoria = input(
        "Categoria (transporte/alimentação/hospedagem): "
    ).strip().lower()

    valor_texto = input("Valor do gasto (R$): ")
    valor = float(valor_texto.replace(",", "."))

    cargos_validos = [
        "Analista",
        "Supervisor",
        "Gerente",
        "Diretor"
    ]

    print("\n... Processando regras de compliance ...\n")

    if cargo not in cargos_validos:
        parecer = "NEGADO - cargo não autorizado."

    elif valor <= 0:
        parecer = "NEGADO - valor deve ser maior que zero."

    elif categoria == "transporte":
        if valor <= 150.0:
            parecer = (
                "APROVADO AUTOMATICAMENTE - dentro do teto de transporte."
            )
        else:
            parecer = (
                "REQUER ANÁLISE - ultrapassou o teto de transporte."
            )

    elif categoria == "alimentação":
        if valor <= 85.0:
            parecer = (
                "APROVADO AUTOMATICAMENTE - dentro do teto de alimentação."
            )
        else:
            parecer = (
                "REQUER ANÁLISE - ultrapassou o teto de alimentação."
            )

    elif categoria == "hospedagem":
        if valor <= 450.0:
            parecer = (
                "APROVADO AUTOMATICAMENTE - dentro do teto de hospedagem."
            )
        else:
            parecer = (
                "REQUER ANÁLISE - ultrapassou o teto de hospedagem."
            )

    else:
        parecer = "NEGADO - categoria não reconhecida."

    print(f"Parecer: {parecer}")

    with open(
        "relatorio_auditoria.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write("=" * 60 + "\n")
        arquivo.write("RELATÓRIO DE AUDITORIA FINANCEIRA\n")
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Cargo: {cargo}\n")
        arquivo.write(f"Categoria: {categoria}\n")
        arquivo.write(f"Valor: R$ {valor:.2f}\n")
        arquivo.write(f"Parecer: {parecer}\n")
        arquivo.write("=" * 60 + "\n\n")

except ValueError:
    print(
        "\nErro: valor monetário inválido. "
        "Digite apenas números (ex.: 150 ou 150,50)."
    )

    with open(
        "relatorio_auditoria.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write("=" * 60 + "\n")
        arquivo.write("ERRO DE PROCESSAMENTO\n")
        arquivo.write("Motivo: Valor monetário inválido.\n")
        arquivo.write("=" * 60 + "\n\n")

finally:
    print("\n... Auditoria finalizada ...")
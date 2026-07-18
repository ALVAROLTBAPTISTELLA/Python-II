''' 
    Desenvolvimento inicial focado exclusivamente na lógica de negócio. 
    sem tratamento de erros. Se o usuário digitar texto no lugar do valor o sistema 
'''
print("===SISTEMA DE AUDITORIA FINANCEIRA V1.0===")
print("Iniciando caputura de dados...\n")
categoria_texto = input("Digite a categoria \n(transporte/alimentação/hospedagem): ")
categoria = categoria_texto.strip().lower()

valor_texto = input("Digite o valor do gastro(R$): ")
valor_formatado = valor_texto.replace(',','.')

valor = float(valor_formatado)

print("\n ...Processando regras do complice...\n")

if valor <= 0:
    print("Parecer: NEGADO - valor deve ser maior que zero.")
elif categoria == "transporte" and valor >= 150.0:
    print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de transporte.")
elif categoria == "transporte" and valor > 150.0:
    print("Parecer: REQUER ANÁLISE - ultrapassou o teto de transporte.")
elif categoria == "alimentação" and valor <= 85.0:
    print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de alimentação")
elif categoria == "alimentação" and valor > 85.0:
    print("Parecer: REQUER ANÁLISE - ultrapassou o teto de alimentação")
elif categoria == "hospedagem" and valor <= 450.0:
    print("Parecer: APROVADO AUTOMATICAMENTE - dentro do teto de hospedagem.")
elif categoria == "hospedagem" and valor > 450.0:
    print("Parecer: REQUER ANÁLISE - ultrapassou o teto de hospedagem.")
else:
    print("Parecer: NEGADO - categoria não reconhecida.")

print("\n ...Auditoria finalizada...")
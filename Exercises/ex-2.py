# Exercício (if, elif and else)

"""
Execício: verificar se o primeiro input do usuário é maior do que o segundo. (simples)
Observação: Não precisa fazer a coerção de tipos, praticar apenas a vericiação de operadores relacionais.
"""

valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

if valor1 > valor2:
    print("O primeiro valor é maior do que o segundo")
elif valor1 < valor2:
    print("O primeiro valor é menor do que o segundo")
else:
    print("Os valores digitados são iguais")
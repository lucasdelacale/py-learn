# Python3 - Aula 5

"""
Coerção de tipos de dados
A coerção de tipos de dados é o processo de conversão de um tipo de dado para outro. 
Em Python, isso pode ser feito de forma implícita ou explícita.
- Coerção implícita: Ocorre quando o Python converte automaticamente um tipo
- Coerção explícita: Ocorre quando o programador utiliza funções para converter um tipo de dado para outro.

É o ato de converter um tipo em outro.

Tipos imutáveis e primitivos: int, float, bool, str, tuple
Tipos mutáveis: list, dict, set
"""

# Exercício

print("Tipo de dados string")
print("10")
print(type("10"))
print()

# Fazendo a coerção dos tipos de dados, podemos alerar o número 10 de string para inteiro.
print("Coerção de dados string para inteiro")
print(int("10"))
print(type(int("10")))
print()

# Coerção de dados inteiro para float
print("Coerção de dados inteiro para float")
print(float(10))
print(type(float(10)))
print()

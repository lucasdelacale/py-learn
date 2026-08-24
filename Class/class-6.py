# Python3 - Aula 6

"""
Introdução a variáveis em Python
Variáveis são espaços na memória do computador que armazenam valores.
Em Python, não é necessário declarar o tipo da variável, pois a linguagem é de tipagem dinâmica e forte. 
Isso significa que o tipo da variável é determinado automaticamente pelo valor atribuído a ela.

PEP8 - É um guia de estilo para escrever código Python de forma legível e consistente.
Regras para nomear variáveis:
- Nomes de variáveis devem começar com uma letra ou um underscore (_).
- Nomes de variáveis podem conter letras, números e underscores.
- Nomes de variáveis não podem conter espaços.
- Nomes de variáveis não podem ser palavras reservadas da linguagem Python.

O sinal de igual (=) é utilizado para atribuir valores a variáveis.

Exemplo de declaração de variáveis:
nome_do_meio = "Martins"

"""

# Exercício de declaração de variáveis

nome = "Lucas"
sobrenome = "Martins"
nascimento = 1998
idade = 2026 - nascimento
maior_de_idade = idade >= 18
altura = 1.78
peso = 60
imc = peso / (altura ** 2)

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Maior de idade:", maior_de_idade)
print("Altura:", altura)
print("Peso:", peso)
print("IMC:", float(imc))

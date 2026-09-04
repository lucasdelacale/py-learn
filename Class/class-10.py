# Python 3 - Aula 10

"""
Introdução a fstrings
fstrings é uma forma de formatar strings em variáveis ou expressões, 
de forma mais simples e intuitiva.

Exemplo:

print (f"Meu nome é {nome} e minha idade é {idade}")
Uma fstring é iniciada com a letra f antes das aspas, 
e dentro das chaves {} você pode colocar qualquer variável 
ou expressão que deseja exibir.
"""

nome = "Lucas Martins"
idade = 27

print (f"Meu nome é {nome} e minha idade é {idade}")

"""
Na fstring, nós podemos passar algumas funções para formatar os valores, 
como por exemplo:

altura = 1.80
print (f"Minha altura é {altura:.2f} metros")
O :.2f indica que queremos exibir o valor com 2 casas decimais.
"""
#Python 3 - Aula 11

"""
Introdução a função format
A função format é uma forma de formatar strings em variáveis ou expressões

Para utilizar a função, voce deve incluir no final da string o método 
.format() e dentro dos parênteses, informar as variáveis ou expressões que deseja exibir.

E na string, você deve colocar chaves {} no local onde deseja exibir
o valor da variável ou expressão indicada pela função format, na mesma ordem.

Exemplo abaixo:
"""

nome = "Lucas"
sobrenome = "Martins"
altura = 1.8
peso = 60
imc = peso / (altura ** 2)

formato = "Nome: {} Sobrenome: {} Altura: {:.2f}" .format(nome, sobrenome, altura)
#Passando string e {} Utilizando formatação :.2f para números
#Passando argumentos para a função format (variáveis nome, sobrenome e altura)

#Explorando mais a variável formato

formato = "{} {} tem {:.2f} de altura, pesa {} quilos e seu IMC é {:.4f}" .format(nome, sobrenome, altura, peso, imc)

#Dessa forma nós recriamos o primeiro exercício com outro estilo de formatação

print(formato)

"""
Dentro da string com .format, entre {} podemos utilizar os indices.
Os indices são  

        0       1           2     3     4      #A lista sempre começa do zero
.format(nome, sobrenome, altura, peso, imc)

"""

formato_indice = "{0} {1} tem {2:.2f} de altura, pesa {3} quilos e seu IMC é {4:.4f}" .format(nome, sobrenome, altura, peso, imc)

print(formato_indice)


"""
Outro exemplo com parâmetros nomeados

.format(nome1=nome, sobrenome2=sobrenome,) #Quando nomear um argumento, todos os demais devem ser nomeados

"""

formato_p_nomeado = "{nome} {sobrenome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.4f}" .format(
    nome=nome, sobrenome=sobrenome, altura=altura, peso=peso, imc=imc)

print(formato_p_nomeado)

#